import pytest
from fastapi.testclient import TestClient
from main import app 
from src.domain.entities import WeatherData

# O TestClient nos permite simular requisições HTTP sem subir o servidor de verdade
client = TestClient(app)

def test_get_weather_endpoint_success(mocker):
    """
    Este teste valida se a ROTA /weather/{city} está funcionando corretamente
    e se a resposta JSON segue o formato esperado.
    """
    # --- ARRANGE ---
    # Criamos um dublê do serviço para isolar o teste da API externa
    mock_service = mocker.Mock()
    
    fake_weather = WeatherData(
        city="Rio de Janeiro", temperature=30.0, description="Ensolarado",
        humidity=60, wind_speed=10.0
    )
    mock_service.execute.return_value = fake_weather
    
    # Injetamos o nosso dublê no estado do App (Injeção de Dependência)
    app.state.weather_service = mock_service

    # --- ACT ---
    # Simulamos uma requisição GET real para o endpoint
    response = client.get("/weather/Rio%20de%20Janeiro")

    # --- ASSERT ---
    # Validamos se o status HTTP é 200 (OK)
    assert response.status_code == 200
    # Validamos se os dados retornados no JSON estão corretos
    data = response.json()
    assert data["city"] == "Rio de Janeiro"
    assert data["temperature"] == 30.0
    assert data["description"] == "Ensolarado"
                        