from fastapi import FastAPI #classe principal
from src.interface.weather_router import router as weather_router

app = FastAPI( #instancia da classe
    title="Weather API Wrapper",
    description="Um serviço de clima com Arquitetura Hexagonal",
    version="1.0.0"
)

app.include_router(weather_router)

@app.get("/health") #leitor de condição de ação
def health_check():
    return {"status": "ok", "message": "Backend rodando!"}

