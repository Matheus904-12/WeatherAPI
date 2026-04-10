# 🌦️ Weather API Wrapper Service

Um serviço fullstack moderno para consulta de previsões meteorológicas, construído com foco em **Clean Code**, **Arquitetura Hexagonal** e **DDD (Domain-Driven Design)**.

![Status do Projeto](https://img.shields.io/badge/Status-Fases%201,%202%20e%203%20Conclu%C3%ADdas-success)
![Tecnologias](https://img.shields.io/badge/Stack-React%20%7C%20TypeScript%20%7C%20FastAPI%20%7C%20Redis-blue)

## 🚀 Sobre o Projeto
Este projeto foi desenvolvido como parte do desafio oficial do **roadmap.sh**. 
**Link do projeto:** [https://roadmap.sh/projects/weather-api-wrapper-service](https://roadmap.sh/projects/weather-api-wrapper-service)

O objetivo é construir uma API que consome um serviço de clima de terceiros (Visual Crossing) e fornece uma interface limpa, performática e cacheada para o usuário final.

---

## 🏗️ Arquitetura do Sistema

O backend foi estruturado utilizando **Arquitetura Hexagonal (Ports & Adapters)** para garantir que a lógica de negócio seja independente de tecnologias externas. No final da Fase 3, implementamos o **Decorator Pattern** para adicionar suporte ao Redis de forma não intrusiva.

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
        A[weather_api_adapter.py]
    end

    R --> UC
    UC --> P
    P -.-> RA
    RA -.-> A
    A --> VC[Visual Crossing API]
    RA --> RD[Redis Cache]
```

---

## ✨ Funcionalidades

### 🎨 Frontend (React + TypeScript)
- **Interface Premium**: Design inspirado no Dribbble com efeitos de Glassmorphism.
- **Internacionalização**: Suporte a traduções (PT-BR) e mapeamento dinâmico de ícones.
- **Animações Dinâmicas**: Ícones de clima animados via SVG e CSS Keyframes.

### ⚙️ Backend (FastAPI + Python)
- **Cache de 12h com Redis**: Otimização de performance e redução de consumo da API externa.
- **Injeção de Dependência**: desacoplamento total entre camadas via `app.state`.
- **Validação Estrita**: Uso de Pydantic para garantir integridade dos dados.

---

## 🛠️ Como Executar

### 1. Iniciar Infraestrutura (Docker)
```bash
docker-compose up -d
```

### 2. Configurar o Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows
pip install -r requirements.txt
```
Crie um arquivo `.env` na pasta `backend/`:
```env
WEATHER_API_KEY=sua_chave_aqui
WEATHER_API_BASE_URL=https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline
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
- [ ] Fase 4: Histórico de Buscas com MongoDB.
- [ ] Fase 5: Testes Automatizados & CI/CD.
- [ ] Fase 6: Debugging Masterclass.
- [ ] Fase 7: Deploy na Azure.
- [ ] Fase 8: Refatoração UI com Ionic Framework.

---
Desenvolvido por **Matheus** como parte do aprendizado avançado em Python, DDD e Clean Code.
