#o que pode ser feito com essa informação

from abc import ABC, abstractmethod #classe base abstrata para criar interfaces
from .entities import WeatherData

class WeatherRepository(ABC): #PORT: contrato de regra de negócio

    @abstractmethod 
    def get_weather(self, city: str) -> WeatherData:
        pass

class HistoryRepository(ABC):
    @abstractmethod
    def save_search(self, weather_data: WeatherData) -> None: #salva a busca no historico
        pass

    @abstractmethod
    def get_all_history(self) -> list[WeatherData]: #recupera todas as buscas salvas
        pass