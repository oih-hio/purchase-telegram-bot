import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

def record_response(spreadsheet_id, sheet_name, chat_id, text):
    creds = Credentials.from_service_account_file(
        os.getenv("GOOGLE_CRED_PATH"),
        scopes=['https://www.googleapis.com/auth/spreadsheets']
    )
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    # отримати всі дані, знайти рядок по chat_id
    data = sheet.values().get(spreadsheetId=spreadsheet_id, range=sheet_name).execute().get('values', [])
    for idx, row in enumerate(data):
        if len(row) > 6 and row[6] == str(chat_id):  # припустимо, chat_id у 7-му стовпці (G)
            row_number = idx + 1
            sheet.values().update(
                spreadsheetId=spreadsheet_id,
                range=f"{sheet_name}!J{row_number}",  # J = 10 стовпець (0-based index 9)
                valueInputOption="RAW",
                body={"values": [[text]]}
            ).execute()
            sheet.values().update(
                spreadsheetId=spreadsheet_id,
                range=f"{sheet_name}!I{row_number}",
                valueInputOption="RAW",
                body={"values": [["відповідь отримано"]]}
            ).execute()
            break
