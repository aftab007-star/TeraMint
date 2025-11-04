from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ai.router import router as ai_router  # 👈 add this line

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 👇 add this line to plug in the AI routes
app.include_router(ai_router)

@app.get("/")
def read_root():
    return {"message": "TeraMint API is running 🚀"}

@app.get("/about")
def about():
    return {"project": "TeraMint", "status": "AI + Tokenized Farming"}
