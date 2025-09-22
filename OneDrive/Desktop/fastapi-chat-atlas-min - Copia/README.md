# Chat em Tempo Real com FastAPI, MongoDB e WebSockets

Este projeto implementa um sistema de **chat em tempo real** utilizando **FastAPI**, **MongoDB Atlas** e **WebSockets**. O código foi refatorado para seguir boas práticas de organização, modularização e manutenibilidade, atendendo aos critérios da atividade proposta.

---

## 🚀 Como rodar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Criar ambiente virtual e instalar dependências

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

### 3. Configurar variáveis de ambiente

Crie um arquivo **.env** na raiz do projeto com base no **.env.example**:

```env
MONGO_URL="sua-string-de-conexao"
MONGO_DB="nome-do-banco"
```

### 4. Executar o servidor

```bash
uvicorn main:app --reload
```

A API estará disponível em: [http://localhost:8000](http://localhost:8000)

---

## 📂 Estrutura do Projeto

```
.
├── main.py              # Inicialização do FastAPI e montagem das rotas
├── config.py            # Configurações externas (.env)
├── database.py          # Conexão com o MongoDB
├── models.py            # Modelos Pydantic e serialização
├── ws_manager.py        # Gerenciamento de conexões WebSocket
├── routes/
│   └── messages.py      # Rotas REST (CRUD de mensagens)
├── requirements.txt     # Dependências
├── .env.example         # Exemplo de configuração
└── README.md            # Documentação do projeto
```

---

## ✅ Checklist de Critérios da Atividade

### Organização em módulos

* [x] `database.py` para conexão com MongoDB
* [x] `models.py` para schemas e serialização
* [x] `ws_manager.py` para gerenciar WebSockets
* [x] `routes/messages.py` para rotas REST
* [x] `main.py` apenas inicializa a aplicação

### Uso de Pydantic

* [x] Criado **MessageIn** para entrada de mensagens
* [x] Criado **MessageOut** para saída de mensagens
* [x] Substituição de `Body(..., embed=True)` pelos modelos

### Tratamento de erros

* [x] Retorno `400 Bad Request` quando `before_id` é inválido
* [x] Bloqueio de mensagens sem conteúdo (erro 400)

### Configurações externas

* [x] Arquivo **config.py** centraliza variáveis de ambiente
* [x] Uso de **python-dotenv** para carregar `.env`

### Documentação mínima

* [x] Docstrings nos principais métodos (`broadcast`, `connect`, etc.)
* [x] Instruções no **README.md** para rodar o projeto
* [x] Arquivo **.env.example** para configuração rápida

---

## 📡 Exemplos de Uso

### 1. REST API – Enviar mensagem

```bash
POST http://localhost:8000/messages
Content-Type: application/json

{
  "sender": "alice",
  "content": "Olá, mundo!"
}
```

**Resposta:**

```json
{
  "id": "650f2c7a3b8f5a1d7e8c1234",
  "sender": "alice",
  "content": "Olá, mundo!",
  "timestamp": "2025-09-22T10:30:00.123456"
}
```

### 2. REST API – Listar mensagens

```bash
GET http://localhost:8000/messages?limit=5
```

**Resposta:**

```json
[
  {
    "id": "650f2c7a3b8f5a1d7e8c1234",
    "sender": "alice",
    "content": "Olá, mundo!",
    "timestamp": "2025-09-22T10:30:00.123456"
  }
]
```

### 3. WebSocket – Conectar e receber mensagens em tempo real

```javascript
const ws = new WebSocket("ws://localhost:8000/ws");

ws.onopen = () => {
  console.log("Conectado ao chat");
  ws.send(JSON.stringify({ sender: "bob", content: "Oi Alice!" }));
};

ws.onmessage = (event) => {
  console.log("Nova mensagem:", event.data);
};
```

**Fluxo esperado:**

* Ao enviar uma mensagem via WebSocket, todos os clientes conectados recebem a atualização em tempo real.

---

## 📌 Observação

Este projeto é uma refatoração para fins acadêmicos, com foco em **organização, modularização e boas práticas** em Python + FastAPI.
