# 🌦️ Weather API Wrapper Service

Um serviço fullstack moderno para consulta de previsões meteorológicas, construído com foco em **Clean Code**, **Arquitetura Hexagonal** e **DDD (Domain-Driven Design)**.

![Status do Projeto](https://img.shields.io/badge/Status-Fases%201%20a%204%20Conclu%C3%ADdas-success)
![Tecnologias](https://img.shields.io/badge/Stack-React%20%7C%20TypeScript%20%7C%20FastAPI%20%7C%20Redis%20%7C%20MongoDB-blue)

## 🚀 Sobre o Projeto
Este projeto foi desenvolvido como parte do desafio oficial do **roadmap.sh**. 
**Link do projeto:** [https://roadmap.sh/projects/weather-api-wrapper-service](https://roadmap.sh/projects/weather-api-wrapper-service)

O objetivo é construir uma API que consome um serviço de clima de terceiros (Visual Crossing) e fornece uma interface limpa, performática e persistente para o usuário final.

---

## 🏗️ Arquitetura do Sistema

O backend utiliza **Arquitetura Hexagonal (Ports & Adapters)** para desacoplar a lógica de negócio das tecnologias externas.

```mermaid
graph TD
    subgraph Interface
        R[weather_router.py]
    end
    subgraph Application
        UC[use_cases.py]
    end
    subgraph Domain
        E[entities.py]
        P[ports.py]
    end
    subgraph Infrastructure
        RA[redis_adapter.py]
        MA[mongo_adapter.py]
        A[weather_api_adapter.py]
    end

    R --> UC
    UC --> P
    P -.-> RA
    P -.-> MA
    RA -.-> A
    A --> VC[Visual Crossing API]
    RA --> RD[Redis Cache]
    MA --> MG[MongoDB History]
```

---

## ✨ Funcionalidades

### 🎨 Frontend (React + TypeScript)
- **Interface Premium**: Design inspirado no Dribbble com efeitos de Glassmorphism.
- **Animações Dinâmicas**: Ícones de clima animados via SVG e CSS.

### ⚙️ Backend (FastAPI + Python)
- **Cache de 12h com Redis**: Otimização de performance.
- **Persistência com MongoDB**: Histórico permanente de todas as buscas realizadas.
- **Alta Resiliência**: Tratamento de falhas de banco (Best Effort).
- **Injeção de Dependência**: desacoplamento total entre camadas via `app.state`.

---

## 🛠️ Como Executar

### 1. Iniciar Infraestrutura (Docker)
```bash
# Sobe Redis e MongoDB
docker-compose up -d
```

### 2. Configurar o Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```
Crie um arquivo `.env` na pasta `backend/`:
```env
WEATHER_API_KEY=sua_chave_aqui
WEATHER_API_BASE_URL=https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline
MONGO_URL=mongodb://localhost:27017
```
Inicie o servidor: `uvicorn main:app --reload`

### 3. Configurar o Frontend
```bash
cd ../frontend
npm install
npm run dev
```

---

## 📅 Roadmap de Evolução
- [x] Fase 1: Interface UI/UX Animada.
- [x] Fase 2: Estrutura Core do Backend.
- [x] Fase 3: Cache de 12h com Redis.
- [x] Fase 4: Histórico de Buscas com MongoDB. ✅
- [ ] Fase 5: Qualidade & Automação (Pytest).
- [ ] Fase 6: Observabilidade & Debugging Masterclass.
- [ ] Fase 7: Deploy na Azure.
- [ ] Fase 8: Refatoração UI com Ionic Framework.

---
Desenvolvido por **Matheus** como parte do aprendizado avançado em Python, DDD e Clean Code.
