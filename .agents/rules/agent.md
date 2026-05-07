# 🤖 Regras Estritas de Orquestração do Agente

Para garantir a integridade do projeto **WeatherAPI**, o Agente (Antigravity) deve seguir estas regras sem exceção:

## 🧭 Gestão de Branches
1.  **Branch Check Automático**: Antes de qualquer comando de escrita, commit ou push, o Agente DEVE validar em qual branch está operando através de `git branch --show-current`.
2.  **Branches de Feature**: Nunca realizar commits diretos na `main`. Sempre criar branches `feat/` ou `fix/` para novas implementações.
3.  **Merge Policy**: Merges para a `main` só devem ocorrer após validação manual do usuário ou após sucesso garantido nos testes.

## 🧪 Qualidade e Testes (CI/CD)
1.  **Test First**: Ao modificar o `use_cases.py` ou o `weather_router.py`, o Agente DEVE sugerir ou criar testes correspondentes.
2.  **Local Test Before Push**: Antes de realizar um `git push`, o Agente DEVE rodar o comando `pytest` localmente para garantir que o pipeline de CI não falhe.
3.  **Ambiente de CI**: Ao atualizar o workflow do GitHub Actions, sempre garantir o uso de variáveis de ambiente "dummy" (falsas) para evitar erros de inicialização de variáveis obrigatórias.

## 📂 Organização de Arquivos
1.  **Pasta .agents**: Utilizar a pasta plural `.agents` para armazenar `rules` e `workflows`.
2.  **Documentação Spec**: Manter os arquivos de arquitetura, features e roadmap dentro de `.agents/workflows/spec/`.

---
*Assinado: Antigravity (Mentor AI)*
