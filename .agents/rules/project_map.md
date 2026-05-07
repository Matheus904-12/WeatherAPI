# Mapa do Projeto (WeatherAPI)

## Estrutura de Camadas (Hexagonal)

### 1. Domain (O Coração)
* `backend/src/domain/entities.py`: Contém a classe `WeatherData`. Regras de negócio puras.
* `backend/src/domain/ports.py`: Define o contrato `WeatherRepository`.

### 2. Application (O Cérebro)
* `backend/src/application/use_cases.py`: Orquestração da lógica de busca de clima.

### 3. Infrastructure (Os Braços)
* `backend/src/infrastructure/weather_api_adapter.py`: Integração com Visual Crossing API.
* `backend/src/infrastructure/redis_adapter.py`: Implementação do Decorator de Cache (Redis).

### 4. Interface (Os Sentidos)
* `backend/src/interface/weather_router.py`: Endpoints FastAPI.
* `frontend/src/`: UI em React + TypeScript.

## Fluxo de Dados
Frontend -> FastAPI Router -> Use Case -> Cache Decorator -> (Redis ou API Adapter)
