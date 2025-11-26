# Como rodar o backend Python para integração com Google Sheets

1. Abra o terminal na pasta `RIO+ELAS/backend-python`.
2. Instale as dependências:

   pip install -r requirements.txt

3. Certifique-se de que o arquivo `plated-field-474017-b8-e00d977b2612.json` está na pasta `RIO+ELAS` (um nível acima do backend-python).
4. Inicie o servidor:

   python app.py

5. O backend ficará disponível em http://localhost:3001

6. No seu HTML, o script já está pronto para enviar para:

   fetch('http://localhost:3001/inscricao', { ... })

Pronto! Ao enviar o formulário, os dados irão para a planilha Google Sheets.
