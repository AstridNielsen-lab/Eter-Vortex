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

#  Proteção Legal

## Direitos Autorais e Propriedade Intelectual

### 1.1. Lei de Direitos Autorais (Brasil)
De acordo com a **Lei nº 9.610/1998** – Lei de Direitos Autorais:
- **Art. 7º**: Protege programas de computador como obras intelectuais.
- **Art. 24º**: Garante direitos morais ao criador.
- **Art. 29º**: Regula cópias e distribuição.

### 1.2. Tratados Internacionais
- **Convenção de Berna (1886)**
- **Acordo TRIPS**
- **Digital Millennium Copyright Act (DMCA)**

## Proteção contra Plágio e Uso Indevido
O uso não autorizado do **Google Dorks Pro** está sujeito a penalidades legais:

- **Art. 184** – Violação de direito autoral (2 a 4 anos de reclusão).
- **Art. 171** – Estelionato e fraude digital (1 a 5 anos).
- **Art. 195** da Lei de Propriedade Industrial.

## Proteção do Código-fonte
- **LGPD (Lei nº 13.709/2018)**
- **Marco Civil da Internet (Lei nº 12.965/2014)**
- **Lei dos Crimes Cibernéticos (Lei nº 12.737/2012)**

- **Privacidade e termos de uso do Google**.
- **LGPD - Lei nº 13.709/2018**.
- **Código Penal Brasileiro - Art. 154-A**.

## Contato para Assuntos Legais

**Julio Campos Machado** (Criador e Desenvolvedor)  
**Empresa**: Like Look Solutions  
**WhatsApp**: +55 11 99294-6628  
**Email**: [juliocamposmachado@gmail.com](mailto:juliocamposmachado@gmail.com)

