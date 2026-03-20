# 🌦️ Weather API Wrapper Service

Um serviço fullstack moderno para consulta de previsões meteorológicas, construído com foco em **Clean Code**, **Arquitetura Hexagonal** e **DDD (Domain-Driven Design)**.

![Status do Projeto](https://img.shields.io/badge/Status-Fase%201%20e%202%20Conclu%C3%ADdas-success)
![Tecnologias](https://img.shields.io/badge/Stack-React%20%7C%20TypeScript%20%7C%20FastAPI-blue)

## 🚀 Sobre o Projeto
Este projeto segue o desafio do [roadmap.sh](https://roadmap.sh/projects/weather-api-wrapper-service). O objetivo é construir um wrapper para APIs de clima, aplicando padrões de arquitetura de software de nível corporativo.

---

## 🎨 Interface (Fase 1) - Concluída ✅
- **UI Premium**: Design inspirado no Dribbble com Glassmorphism.
- **Animações Fluidas**: Ícones meteorológicos animados via SVG e CSS Keyframes.
- **Responsividade**: Experiência mobile-first refinada.

---

## 🏗️ Backend (Fase 2) - Concluído ✅
Implementado seguindo a **Arquitetura Hexagonal (Ports and Adapters)**:
- **Domain**: Entidades puras ([WeatherData](cci:2://file:///home/bcr/Projetos/Atividades/Pessoal/WeatherAPI/frontend/src/App.tsx:34:0-41:1)) e contratos ([WeatherRepository](cci:2://file:///home/bcr/Projetos/Atividades/Pessoal/WeatherAPI/backend/src/domain/ports.py:5:0-9:12)).
- **Application**: Casos de uso orquestrados ([GetWeatherUseCase](cci:2://file:///home/bcr/Projetos/Atividades/Pessoal/WeatherAPI/backend/src/application/use_cases.py:3:0-12:48)).
- **Infrastructure**: Integração real com a API **Visual Crossing** via `httpx`.
- **Interface**: Endpoints FastAPI com documentação automática via **Swagger UI** (`/docs`).

### ⚙️ Como Rodar o Backend
1. Entre na pasta: `cd backend`
2. Ative o venv: `source venv/bin/activate`
3. Instale as dependências: `pip install -r requirements.txt`
4. Crie o arquivo `.env` com sua chave:
   ```env
   WEATHER_API_KEY=sua_chave_aqui
   WEATHER_API_BASE_URL=https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline
