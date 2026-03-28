from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func, select
from datetime import datetime, timedelta
import random
from app.db.session import get_db
from app.deps import get_current_user
from app.db.models import Task

router = APIRouter(prefix="/metrics", tags=["metrics"])

@router.get("/summary")
def summary(db: Session = Depends(get_db), user=Depends(get_current_user)):
    total = db.execute(select(func.count()).select_from(Task).where(Task.owner_id == user.id)).scalar_one()
    done = db.execute(select(func.count()).select_from(Task).where(Task.owner_id == user.id, Task.status == "done")).scalar_one()

    days = 14
    today = datetime.utcnow().date()
    revenue = []
    v = 1200 + random.randint(-150, 150)
    for i in range(days):
        day = today - timedelta(days=(days - 1 - i))
        v = max(300, v + random.randint(-120, 140))
        revenue.append({"day": day.strftime("%m-%d"), "value": v})

    return {
        "kpis": [
            {"label": "Tasks", "value": str(total), "delta": "+3.1%"},
            {"label": "Done", "value": str(done), "delta": "+1.2%"},
            {"label": "Completion", "value": f"{(done/total*100):.0f}%" if total else "0%", "delta": "+0.7%"},
        ],
        "revenue": revenue,
        "topPages": [{"path": "/dashboard", "views": 1821}, {"path": "/tasks", "views": 1219}, {"path": "/settings", "views": 544}],
    }
