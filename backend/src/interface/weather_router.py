from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.application.use_cases import GetWeatherUseCase
from src.infrastructure.weather_api_adapter import VisualCrossingAdapter
from fastapi import APIRouter, HTTPException, Request

router = APIRouter(prefix="/weather", tags=["Clima"])

class WeatherResponse(BaseModel):
    city: str
    temperature: float
    description: str
    humidity: float
    wind_speed: float

@router.get("/{city}")
async def get_weather(city: str, request: Request):
    try:
        # O serviço já vem injetado com Cache e Mongo do main.py
        weather_service = request.app.state.weather_service
        data = weather_service.execute(city)
        return data
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        print(f"Erro real: {e}")
        raise HTTPException(status_code=502, detail="Erro ao consultar API de clima.")