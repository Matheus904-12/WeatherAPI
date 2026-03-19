# 🌦️ Weather API Wrapper Service

Um serviço fullstack moderno para consulta de previsões meteorológicas, construído com foco em **Clean Code**, **Arquitetura Hexagonal** e **DDD (Domain-Driven Design)**.

![Status do Projeto](https://img.shields.io/badge/Status-Fase%201%20Conclu%C3%ADda-success)
![Tecnologias](https://img.shields.io/badge/Stack-React%20%7C%20TypeScript%20%7C%20FastAPI-blue)

## 🚀 Sobre o Projeto
Este projeto faz parte do desafio [Weather API Wrapper Service](https://roadmap.sh/projects/weather-api-wrapper-service) do roadmap.sh. O objetivo é criar um serviço que consome dados de clima de APIs externas (como Visual Crossing), implementa cache inteligente e oferece uma interface de usuário premium.

---

## 🎨 Interface (Fase 1)
A interface foi inspirada em designs modernos do Dribbble, utilizando:
- **Glassmorphism**: Efeito de vidro fosco com transparência e desfoque.
- **Micro-animações**: Ícones de Sol e Chuva animados via SVG + CSS.
- **Responsividade**: Layout totalmente adaptado para dispositivos móveis.
- **TypeScript**: Tipagem estrita para segurança e previsibilidade dos dados.

---

## 🏗️ Arquitetura (Fase 2 - Em breve)
O backend será construído utilizando **FastAPI** e seguirá a **Arquitetura Hexagonal**:
- `Domain`: Regras de negócio puras e entidades.
- `Application`: Casos de uso e orquestração.
- `Infrastructure`: Adaptadores para APIs externas e Cache (Redis).
- `Interface`: Endpoints da API e Schemas.

---

## 🛠️ Como rodar o projeto

### Frontend
1. Entre na pasta: `cd frontend`
2. Instale as dependências: `npm install`
3. Inicie o servidor: `npm run dev`

### Backend (Em desenvolvimento)
1. Entre na pasta: `cd backend`
2. Ative o ambiente virtual: `source venv/bin/activate`
3. Instale as dependências: `pip install -r requirements.txt`

---

## 🌐 Hospedagem (Vercel)
A interface deste projeto está hospedada na [Vercel](https://vercel.com).
