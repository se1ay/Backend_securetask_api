from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select, func
from app.db.session import get_db
from app.db.models import Task
from app.deps import get_current_user
from app.schemas import TaskIn, TaskOut, TaskUpdate, Page

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("", response_model=TaskOut)
def create_task(payload: TaskIn, db: Session = Depends(get_db), user=Depends(get_current_user)):
    t = Task(title=payload.title, description=payload.description, owner_id=user.id)
    db.add(t); db.commit(); db.refresh(t)
    return TaskOut(id=t.id, title=t.title, description=t.description, status=t.status)

@router.get("", response_model=Page)
def list_tasks(limit: int = 20, offset: int = 0, db: Session = Depends(get_db), user=Depends(get_current_user)):
    q = db.execute(select(Task).where(Task.owner_id == user.id).order_by(Task.id.desc()).limit(limit).offset(offset)).scalars().all()
    total = db.execute(select(func.count()).select_from(Task).where(Task.owner_id == user.id)).scalar_one()
    items = [TaskOut(id=t.id, title=t.title, description=t.description, status=t.status) for t in q]
    return Page(items=items, total=total, limit=limit, offset=offset)

@router.get("/{task_id}", response_model=TaskOut)
def get_task(task_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    t = db.query(Task).filter(Task.id == task_id, Task.owner_id == user.id).first()
    if not t: raise HTTPException(404, "Not found")
    return TaskOut(id=t.id, title=t.title, description=t.description, status=t.status)

@router.patch("/{task_id}", response_model=TaskOut)
def update_task(task_id: int, payload: TaskUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    t = db.query(Task).filter(Task.id == task_id, Task.owner_id == user.id).first()
    if not t: raise HTTPException(404, "Not found")
    if payload.title is not None: t.title = payload.title
    if payload.description is not None: t.description = payload.description
    if payload.status is not None: t.status = payload.status
    db.commit(); db.refresh(t)
    return TaskOut(id=t.id, title=t.title, description=t.description, status=t.status)

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    t = db.query(Task).filter(Task.id == task_id, Task.owner_id == user.id).first()
    if not t: raise HTTPException(404, "Not found")
    db.delete(t); db.commit()
    return {"ok": True}
