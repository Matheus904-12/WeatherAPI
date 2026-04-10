import httpx
import os
from src.domain.ports import WeatherRepository
from src.domain.entities import WeatherData

class VisualCrossingAdapter(WeatherRepository):

    def __init__(self):
        self.api_key = os.getenv("WEATHER_API_KEY")
        self.base_url = os.getenv("WEATHER_API_BASE_URL")
    
    def get_weather(self, city: str) -> WeatherData:
        url = f"{self.base_url}/{city}"
        params = {
            "unitGroup": "metric",
            "key": self.api_key,
            "contentType": "json",
            "include": "current"
        }

        response = httpx.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        current = data["currentConditions"]

        return WeatherData(
            city=data["resolvedAddress"],
            temperature=current["temp"],
            description=current["conditions"],
            humidity=current["humidity"],
            wind_speed=current["windspeed"]
        )