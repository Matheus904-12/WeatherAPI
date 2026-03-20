#o que é esse dado desta informação

from dataclasses import dataclass

@dataclass #formata o dado para receber informações
class WeatherData: #Entidade
    city: str
    temperature: float
    description: str
    humidity: float
    wind_speed: float