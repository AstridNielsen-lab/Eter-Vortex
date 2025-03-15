# Projeto Adi – Eter Vortex

![Eter Vortex Logo](https://raw.githubusercontent.com/AstridNielsen-lab/Eter-Vortex/refs/heads/index/like%20look.gif) <!-- Adicione um logo se disponível -->

## Descrição

O "Projeto Adi – Eter Vortex" é uma ferramenta de automação inteligente projetada para coletar dados de leads e facilitá-los através de um painel web interativo. Utilizando módulos de IA, a aplicação coleta números de WhatsApp, e-mails, websites e palavras-chave, automatizando o contato e o suporte por meio de mensagens e chamadas.

## Funcionalidades

- **Coleta Automática de Dados**: Coleta de WhatsApp, e-mails, sites e palavras-chave.
- **Banco de Dados**: Armazenamento na nuvem com Firestore ou PostgreSQL.
- **Painel Web Interativo**: Visualização dos dados coletados com gráficos e estatísticas.
- **Automação via WhatsApp**: Envio de mensagens e consultas automatizadas.
- **Integração com IA Gemini**: Respostas rápidas e personalizadas para interações.
- **URA (Unidade de Resposta Audível)**: Funcionalidade para chamadas automáticas e interativas.

## Estrutura de Diretórios

```
projeto_automacao
├── modules          # Módulos de IA para coleta de dados
│   ├── ia_whatsapp.py     # Busca números do WhatsApp
│   ├── ia_emails.py       # Busca e-mails
│   ├── ia_websites.py     # Busca sites relevantes
│   ├── ia_palavraschave.py # Busca palavras-chave
├── database         # Banco de dados (Firestore ou SQLite)
├── services         # Serviços externos (Twilio, APIs)
├── web              # Aplicação web (Flask + Dash)
│   ├── app.py               # Servidor Flask
│   ├── dashboard.py         # Dashboard interativa
│   ├── templates/index.html  # Página inicial
│   ├── static/style.css      # Estilos da página
├── requirements.txt # Dependências do projeto
└── wsgi.py          # Arquivo para rodar no PythonAnywhere

```

## Tecnologias Usadas

- Python
- Flask
- Dash
- PostgreSQL / Firestore
- Twilio
- API Google Gemini
