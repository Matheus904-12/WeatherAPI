import redis
import json 
from src.domain.ports import WeatherRepository
from src.domain.entities import WeatherData

class CacheWeatherRepository(WeatherRepository):
    def __init__(self, real_repository: WeatherRepository, redis_client: redis.Redis):
        self.real_repository = real_repository
        self.redis = redis_client
        self.ttl = 43200 #12 horas

    def get_weather(self, city: str) -> WeatherData:
        cache_key = f"weather:{city.lower().strip()}"

        cache_data = self.redis.get(cache_key)

        if cache_data:
            print(f"* Cache Hit para {city}")
            data = json.loads(cache_data)
            return WeatherData(**data)

        print(f"Cache Miss para: {city}. Buscando na API externa...")
        weather = self.real_repository.get_weather(city)

        self.redis.setex(
            cache_key,
            self.ttl,
            json.dumps(weather.__dict__)
        )
        return weather