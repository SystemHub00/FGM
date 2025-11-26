import express from 'express';
import cors from 'cors';
import { GoogleSpreadsheet } from 'google-spreadsheet';
import path from 'path';
import { fileURLToPath } from 'url';
import fs from 'fs';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
app.use(cors());
app.use(express.json());

// Caminho para a chave de serviço
const CREDENTIALS_PATH = path.join(__dirname, '../plated-field-474017-b8-e00d977b2612.json');
// ID da planilha
const SHEET_ID = '1ZPJuyANbc6YBJzcNOVXqzsu0d4uNKy2c3nSYHR-UaAk';

app.post('/inscricao', async (req, res) => {
  try {
    const creds = JSON.parse(fs.readFileSync(CREDENTIALS_PATH));
    const doc = new GoogleSpreadsheet(SHEET_ID);
    await doc.useServiceAccountAuth(creds);
    await doc.loadInfo();
    const sheet = doc.sheetsByIndex[0];

    // Os campos devem bater com os nomes dos inputs do HTML
    const { nome, email, telefone, curso, idade, bairro } = req.body;
    await sheet.addRow({ nome, email, telefone, curso, idade, bairro });

    res.json({ result: 'success' });
  } catch (err) {
    console.error(err);
    res.status(500).json({ result: 'error', message: err.message });
  }
});

const PORT = 3001;
app.listen(PORT, () => {
  console.log(`Servidor rodando em http://localhost:${PORT}`);
});
