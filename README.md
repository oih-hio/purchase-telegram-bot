# Telegram Return Bot for Repairs

## 🛠 Description
Flask+Telegram bot with webhook that:
- надсилає повідомлення при “так” в стовпці H
- приймає відповідь і записує у стовпець J
- оновлює статус у I

## ✅ Setup

1. Створи `credentials.json` (service account)
2. Відкрий доступ до таблиці сервісному акаунту
3. Створи `.env` з параметрами
4. Деплой на Railway:
   - додай змінні env
   - запусти Deploy
5. Після деплою виконай:
```python
import requests
TOKEN = "<твій токен>"
URL = "<твій webhook URL>/webhook"
requests.post(f"https://api.telegram.org/bot{TOKEN}/setWebhook", data={'url': URL})
