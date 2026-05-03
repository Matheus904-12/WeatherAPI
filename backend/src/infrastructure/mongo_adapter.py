from pymongo import MongoClient
from src.domain.ports import HistoryRepository
from src.domain.entities import WeatherData
import datetime

class MongoHistoryRepository(HistoryRepository):
    def __init__(self, connection_string: str):
        self.client = MongoClient(connection_string)
        self.db = self.client["weather_db"]
        self.collection = self.db["search_history"]

    def save_search(self, weather_data: WeatherData) -> None:
        document = weather_data.__dict__.copy()
        document["timestamp"] = datetime.datetime.utcnow()
        
        self.collection.insert_one(document)
        print(f"Historico salvo no MongoDB para: {weather_data.city}")

    def get_all_history(self) -> list[WeatherData]:
        cursor = self.collection.find().sort("timestamp", -1)

        history = []
        for doc in cursor:
            doc.pop("_id", None)
            doc.pop("timestamp", None)
            history.append(WeatherData(**doc))

        return history