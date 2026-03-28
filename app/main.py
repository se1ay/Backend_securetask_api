from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routes.auth import router as auth
from app.routes.tasks import router as tasks
from app.routes.metrics import router as metrics

app = FastAPI(title="SecureTask API", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_list(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth)
app.include_router(tasks)
app.include_router(metrics)

@app.get("/health")
def health():
    return {"ok": True}
