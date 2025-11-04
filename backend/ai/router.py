# backend/ai/router.py

from fastapi import APIRouter
from .service import run_lambgpt, health_check

router = APIRouter(prefix="/ai", tags=["ai"])

@router.get("/health")
def ai_health():
    return health_check()

@router.post("/lambgpt")
def ai_lambgpt(prompt: str):
    return run_lambgpt(prompt)
