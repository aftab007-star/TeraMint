# backend/ai/service.py

from datetime import datetime

def run_lambgpt(prompt: str) -> dict:
    """
    Mock AI worker. Later we can swap this with real model / OpenAI / local YOLO pipeline.
    """
    return {
        "bot": "LambGPT",
        "prompt": prompt,
        "analysis": "Lambs look healthy. No stress patterns detected.",
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }

def health_check() -> dict:
    return {
        "ai_layer": "ok",
        "bots_available": ["LambGPT"],
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }
