from src.domain.ports import WeatherRepository #Injeção de dependência = não sabe de onde vem mas sabe o que deve ser seguido
from src.domain.entities import WeatherData

class GetWeatherUseCase:

    def __init__(self, repository: WeatherRepository):
        self.repository = repository

    def execute(self, city: str) -> WeatherData:
        if not city or not city.strip():
            raise ValueError("O nome da cidade não pode ser vazio.")
        
        return self.repository.get_weather(city)