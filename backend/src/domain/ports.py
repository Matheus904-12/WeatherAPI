#o que pode ser feito com essa informação

from abc import ABC, abstractmethod #classe base abstrata para criar interfaces
from .entities import WeatherData

class WeatherRepository(ABC): #PORT: contrato de regra de negócio

    @abstractmethod 
    def get_weather(self, city: str) -> WeatherData:
        pass