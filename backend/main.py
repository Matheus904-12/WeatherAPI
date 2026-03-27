from fastapi import FastAPI #classe principal
from src.interface.weather_router import router as weather_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI( #instancia da classe
    title="Weather API Wrapper",
    description="Um serviço de clima com Arquitetura Hexagonal",
    version="1.0.0"
)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(weather_router)

@app.get("/health") #leitor de condição de ação
def health_check():
    return {"status": "ok", "message": "Backend rodando!"}

