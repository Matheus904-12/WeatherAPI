# Funcionalidades do WeatherAPI

## 1. Busca de Clima por Cidade
- **Descrição**: O usuário digita o nome de uma cidade no frontend e recebe os dados climáticos atuais.
- **Campos Retornados**: Cidade, Temperatura (°C), Descrição, Umidade e Velocidade do Vento.
- **Tradução**: O sistema mapeia os dados da API original para o português brasileiro.

## 2. Cache Inteligente
- **Descrição**: Evita chamadas repetitivas à API externa.
- **Duração**: 12 horas.
- **Tecnologia**: Redis rodando em contêiner Docker.
- **Log**: O sistema informa no terminal se ocorreu um `Cache Hit` ou `Cache Miss`.

## 3. Interface Animada
- **Descrição**: UI moderna com Glassmorphism inspirado no Dribbble.
- **Ícones**: Mapeamento dinâmico de ícones animados baseado nas condições climáticas.
