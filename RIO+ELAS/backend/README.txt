# Como rodar o backend Node.js para integração com Google Sheets

1. Abra o terminal na pasta `RIO+ELAS/backend`.
2. Instale as dependências:

    npm install

3. Certifique-se de que o arquivo `plated-field-474017-b8-e00d977b2612.json` está na pasta `RIO+ELAS` (um nível acima do backend).
4. Inicie o servidor:

    npm start

5. O backend ficará disponível em http://localhost:3001

6. No seu HTML, altere o script para enviar para:

    fetch('http://localhost:3001/inscricao', { ... })

Pronto! Ao enviar o formulário, os dados irão para a planilha Google Sheets.
