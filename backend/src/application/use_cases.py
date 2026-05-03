from src.domain.ports import WeatherRepository, HistoryRepository #Injeção de dependência = não sabe de onde vem mas sabe o que deve ser seguido
from src.domain.entities import WeatherData

class GetWeatherUseCase:

    def __init__(self, weather_repo: WeatherRepository, history_repo: HistoryRepository):
        self.weather_repo = weather_repo
        self.history_repo = history_repo

    def execute(self, city: str) -> WeatherData:
        if not city or not city.strip():
            raise ValueError("O nome da cidade não pode ser vazio.")

        weather = self.weather_repo.get_weather(city)

        self.history_repo.save_search(weather)
        
        return weather