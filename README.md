# secretar.IA-consultorio-medico

Sistema de agendamento de consultas via chat com integração a IA e Google Agenda.

## Requisitos

- Python 3.10+
- Dependências listadas em `requirements.txt`

Instale com:

```bash
pip install -r requirements.txt
```

## Executando o servidor

```bash
python backend/server.py
```

A aplicação servirá um WebSocket em `ws://localhost:8765` consumido pelo frontend.

Abra `frontend/index.html` em seu navegador para testar a comunicação.

## Funcionalidades

- Chat simples em HTML/JavaScript
- Servidor Python com WebSocket
- Módulos para integração com Google Calendar (placeholders)

Este projeto é um esqueleto inicial para futura integração com LangFlow e OpenAI.
