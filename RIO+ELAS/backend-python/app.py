from flask import Flask, request, jsonify
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import os

app = Flask(__name__)

# Caminho para a chave de serviço
SERVICE_ACCOUNT_FILE = os.path.join(os.path.dirname(__file__), '../plated-field-474017-b8-e00d977b2612.json')
# ID da planilha
SPREADSHEET_ID = '1ZPJuyANbc6YBJzcNOVXqzsu0d4uNKy2c3nSYHR-UaAk'
# Nome da aba (padrão: primeira aba)
SHEET_NAME = 'Sheet1'

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

@app.route('/inscricao', methods=['POST'])
def inscricao():
    data = request.get_json()
    values = [[
        data.get('nome', ''),
        data.get('email', ''),
        data.get('telefone', ''),
        data.get('curso', ''),
        data.get('idade', ''),
        data.get('bairro', '')
    ]]
    try:
        creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        sheet.values().append(
            spreadsheetId=SPREADSHEET_ID,
            range=f"{SHEET_NAME}!A:F",
            valueInputOption="RAW",
            body={"values": values}
        ).execute()
        return jsonify({'result': 'success'})
    except Exception as e:
        return jsonify({'result': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(port=3001, debug=True)
