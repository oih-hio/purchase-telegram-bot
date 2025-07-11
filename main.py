from flask import Flask, request
import os
import requests
from gsheets_helper import record_response

TOKEN = os.getenv("TELEGRAM_TOKEN")
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
SHEET_NAME = os.getenv("SHEET_NAME", "Povernenja_v_remont")

TELEGRAM_API = f"https://api.telegram.org/bot{TOKEN}"
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if 'message' in data:
        msg = data['message']
        chat_id = msg['chat']['id']
        text = msg.get('text', '')
        message_id = msg['message_id']

        # запис у Google Sheet
        record_response(SPREADSHEET_ID, SHEET_NAME, chat_id, text)

        # відправка підтвердження
        requests.post(f"{TELEGRAM_API}/sendMessage", json={
            'chat_id': chat_id,
            'text': f"Дякую! Відповідь записана: {text}",
            'reply_to_message_id': message_id
        })

    return "ok", 200

@app.route('/')
def home():
    return "Bot is running!"

if __name__ == '__main__':
    app.run(debug=True)
