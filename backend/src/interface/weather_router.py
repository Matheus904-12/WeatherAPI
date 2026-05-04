from fastapi import APIRouter, HTTPException, Request 
from pydantic import BaseModel


router = APIRouter(prefix="/weather", tags=["Clima"])

class WeatherResponse(BaseModel):
    city: str
    temperature: float
    description: str
    humidity: float
    wind_speed: float

@router.get("/{city}", response_model=WeatherResponse)
def get_weather(city: str, request: Request):
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

@router.get("/history/all", response_model=list[WeatherResponse])
def get_history(request: Request):
    try:
        weather_service = request.app.state.weather_service
        history = weather_service.history_repo.get_all_history()

        return history
    except Exception as e:
        print(f"Erro ao buscar historico: {e}")
        raise HTTPException(status_code=500, detail="Erro ao recuperar histórico.")