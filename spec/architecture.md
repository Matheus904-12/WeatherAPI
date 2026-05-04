# Especificação: Arquitetura Hexagonal & DDD

## Visão Geral
O projeto utiliza **Arquitetura Hexagonal** para isolar a lógica de negócio de detalhes técnicos como bancos de dados ou APIs externas.

## Princípios Aplicados
1. **Inversão de Dependência**: O Use Case depende de uma abstração (`WeatherRepository`) e não de uma classe concreta.
2. **Ports & Adapters**: 
    - **Port**: Interface que define o que o sistema precisa.
    - **Adapter**: Implementação técnica de um Port.
3. **Decorator Pattern**: Utilizado no Redis para adicionar cache sem modificar a lógica original da API.

## Tecnologias
- **FastAPI**: Interface de entrada.
- **Pydantic**: Validação de contratos de dados.
- **Redis**: Cache de curta duração (12h).
- **Httpx**: Cliente HTTP assíncrono para consumo de APIs.
