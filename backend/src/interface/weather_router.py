from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.application.use_cases import GetWeatherUseCase
from src.infrastructure.weather_api_adapter import VisualCrossingAdapter

router = APIRouter(prefix="/weather", tags=["Clima"])

class WeatherResponse(BaseModel):
    city: str
    temperature: float
    description: str
    humidity: float
    wind_speed: float

@router.get("/{city}", response_model=WeatherResponse)
def get_weather(city: str):
    try:
        adapter = VisualCrossingAdapter()
        use_case = GetWeatherUseCase(repository=adapter)
        result = use_case.execute(city)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=502, detail="Erro ao consultar API de clima.")