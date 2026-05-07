from apscheduler.schedulers.background import BackgroundScheduler
from src.application.use_cases import GetWeatherUseCase

CITIES_TO_WATCH = ["São Paulo", "Londres", "Nova York", "Tóquio"]

def setup_weather_scheduler(weather_service: GetWeatherUseCase):
    scheduler = BackgroundScheduler()

    def fetch_all_watched_cities():
        print(f"Robo Coletor: Iniciando busca para {len(CITIES_TO_WATCH)} cidades...")
        for city in CITIES_TO_WATCH:
            try:
                weather_service.execute(city)
                print(f"Clima de {city} coletado e persistido.")
            except Exception as e:
                print(f"Erro ao coletar {city}: {e}")

    scheduler.add_job(fetch_all_watched_cities, 'interval', minutes=60)

    scheduler.start()

    return scheduler