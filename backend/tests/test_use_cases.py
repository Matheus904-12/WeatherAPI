import pytest
from src.application.use_cases import GetWeatherUseCase
from src.domain.entities import WeatherData

# Teste 1: Garante que o fluxo principal funciona quando os dados são válidos
def tests_get_weather_sucess(mocker):
    # --- ARRANGE (Preparação) ---
    # Criamos "dublês" (mocks) para não depender de banco de dados ou API real
    mock_weather_repo = mocker.Mock()
    mock_history_repo = mocker.Mock()

    # Simulamos um retorno de clima vindo do "dublê" da API
    fake_weather = WeatherData(
        city="Paris", temperature=15.0, description="Nuvens", humidity=80, wind_speed=5.0
    )
    mock_weather_repo.get_weather.return_value = fake_weather

    # Injetamos os dublês no Use Case (Injeção de Dependência)
    use_case = GetWeatherUseCase(mock_weather_repo, mock_history_repo)

    # --- ACT (Ação) ---
    # Executamos a lógica que queremos testar
    result = use_case.execute("Paris")

    # --- ASSERT (Verificação) ---
    # Validamos se o resultado é o esperado
    assert result.city == "Paris"
    assert result.temperature == 15.0
    # Importante: Garantimos que o histórico foi SALVO no banco de dados (Mongo)
    mock_history_repo.save_search.assert_called_once_with(fake_weather)


# Teste 2: Garante que o sistema barra erros antes de gastar recursos (API/Banco)
def test_get_weather_empty_city_raises_error(mocker):
    # --- ARRANGE ---
    mock_weather_repo = mocker.Mock()
    mock_history_repo = mocker.Mock()
    use_case = GetWeatherUseCase(mock_weather_repo, mock_history_repo)

    # --- ACT & ASSERT ---
    # Verificamos se o sistema lança um erro (ValueError) ao receber cidade vazia
    with pytest.raises(ValueError, match="O nome da cidade não pode ser vazio"):
        use_case.execute("  ")

    # Verificamos que a API de clima NUNCA foi chamada (evita gastos desnecessários)
    mock_weather_repo.get_weather.assert_not_called()
