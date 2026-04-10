import os
import redis
from dotenv import load_dotenv
from fastapi import FastAPI
from src.interface.weather_router import router as weather_router
from fastapi.middleware.cors import CORSMiddleware
from src.infrastructure.redis_adapter import CacheWeatherRepository
from src.infrastructure.weather_api_adapter import VisualCrossingAdapter
from src.application.use_cases import GetWeatherUseCase

load_dotenv()

REQUIRED_ENV_VARS = ["WEATHER_API_KEY", "WEATHER_API_BASE_URL"]

missing_vars = [var for var in REQUIRED_ENV_VARS if not os.getenv(var)]
if missing_vars:
    raise RuntimeError(
        f"Missing required environment variables: {', '.join(missing_vars)}. "
        f"Please check your .env file and copy from .env.example"
    )

app = FastAPI(
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

redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
api_adapter = VisualCrossingAdapter()
cached_repo = CacheWeatherRepository(api_adapter, redis_client)
weather_service = GetWeatherUseCase(cached_repo)
app.state.weather_service = weather_service

app.include_router(weather_router)

@app.get("/health") #leitor de condição de ação
def health_check():
    return {"status": "ok", "message": "Backend rodando!"}

