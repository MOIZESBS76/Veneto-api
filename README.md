# 🍕 Veneto - Sistema de Gestão de Pedidos para Pizzaria

Bem-vindo ao repositório da Veneto API! Este projeto implementa um sistema de backend robusto para gerenciar pedidos de uma pizzaria, focando na eficiência e escalabilidade. Desenvolvido com Python e FastAPI, a API oferece endpoints para gerenciamento de produtos e pedidos, com persistência de dados em MongoDB.

---

## 🚦 Status do Projeto

O backend da Veneto API está **100% funcional** e pronto para integração com aplicações frontend ou outros serviços.

### ✅ Features Implementadas e Testadas

| Feature                                | Status | Notas                                                 |
| :------------------------------------- | :----- | :---------------------------------------------------- |
| Estrutura base do projeto              | ✅ Completo | Padrão DDD e organização clara.                       |
| Endpoints de Produtos (Listar, Filtrar) | ✅ Completo | Listagem de todos os produtos e produtos por categoria. |
| Endpoints de Pedidos (CRUD)            | ✅ Completo | Criação, listagem e atualização de status de pedidos. |
| Conexão com MongoDB                    | ✅ Completo | Persistência de dados em MongoDB Atlas/Local.         |
| Documentação Swagger UI                | ✅ Completo | Interface interativa em `/docs` e `/redoc`.         |
| README.md com instruções de setup      | ✅ Completo | Este arquivo detalhado.                               |
| Resolução de Erros de Validação        | ✅ Completo | `id` gerado automaticamente, `notes` string vazia.    |
| Configuração de Variáveis de Ambiente  | ✅ Completo | Uso de `.env` para configurações sensíveis.           |

---

## 🚀 Stack Tecnológico

Este projeto foi construído utilizando as seguintes tecnologias:

-   **Linguagem**: Python 3.12 🐍
-   **Framework Web**: FastAPI (com Pydantic para validação de dados) ✨
-   **Servidor ASGI**: Uvicorn
-   **Banco de Dados**: MongoDB 🍃
-   **Driver MongoDB Async**: Motor
-   **Gerenciador de Dependências**: `pip`

---

## 📁 Estrutura do Projeto

A organização do projeto segue um padrão Domain-Driven Design (DDD) para modularidade e clareza:
├── app/ │ ├── api/ # Camada de API (Endpoints, Rotas, Modelos de Request/Response) │ │ ├── deps.py # Dependências para injeção de serviços │ │ └── routers/ # Definição dos endpoints da API │ │ ├── init.py │ │ ├── orders.py # Rotas para pedidos │ │ └── products.py # Rotas para produtos │ ├── core/ # Configurações globais e inicialização │ │ ├── config.py # Variáveis de ambiente e configurações │ │ └── database.py # Configuração da conexão com MongoDB │ ├── domain/ # Lógica de Negócios (Entidades, Modelos, Regras de Domínio) │ │ ├── init.py │ │ ├── order_entities.py # Modelos Pydantic para pedidos │ │ └── product_entities.py # Modelos Pydantic para produtos │ ├── services/ # Serviços de Aplicação (Lógica de Negócios orquestrada) │ │ ├── init.py │ │ └── order_service.py # Lógica de negócio para pedidos │ │ └── product_service.py # Lógica de negócio para produtos │ └── main.py # Ponto de entrada da aplicação FastAPI ├── scripts/ │ ├── init.py │ └── seed_mongodb.py # Script para popular o MongoDB com dados iniciais ├── .env.example # Exemplo de arquivo de variáveis de ambiente ├── docker-compose.yml # Configuração para Docker Compose (MongoDB) ├── README.md # Este arquivo ├── requirements.txt # Lista de dependências do Python └── venv/ # Ambiente virtual (gerado automaticamente)

--- ## ⚙️ Requisitos Antes de iniciar, certifique-se de ter os seguintes softwares instalados: - **Python 3.12+** - **MongoDB**: Uma instância rodando (local ou MongoDB Atlas). Para desenvolvimento local, recomendamos usar Docker. - **pip**: Gerenciador de pacotes do Python (geralmente vem com o Python). - **Docker** (opcional, para rodar MongoDB localmente). --- ## 🚀 Instalação Siga os passos abaixo para configurar e rodar o projeto localmente: 1. **Clonar o repositório:** ```bash git clone https://github.com/seu-usuario/veneto-api.git cd veneto-api ``` 2. **Criar e ativar o ambiente virtual:** ```bash python -m venv venv # No Windows .\venv\Scripts\Activate # No macOS/Linux source venv/bin/activate ``` 3. **Instalar as dependências:** ```bash pip install -r requirements.txt ``` *Se tiver problemas com `pip`, tente:* ```bash python -m pip install -r requirements.txt # ou & ".\venv\Scripts\python.exe" -m pip install -r requirements.txt ``` --- ## 🔒 Configuração Crie um arquivo `.env` na raiz do projeto (copiando `.env.example`) e configure as variáveis de ambiente: ```ini # .env MONGO_URI="mongodb://localhost:27017/veneto_db" # Ou sua URI do MongoDB Atlas: # MONGO_URI="mongodb+srv://<user>:<password>@<cluster-url>/veneto_db?retryWrites=true&w=majority"
▶️ Como Executar
Subir o MongoDB (via Docker - opcional):

bash


docker-compose up -d
Certifique-se de que a MONGO_URI no seu .env aponte para mongodb://localhost:27017/veneto_db.

Popular o banco de dados (se necessário):

bash


python scripts/seed_mongodb.py
Rodar a API:

bash


python -m uvicorn app.main:app --reload
A API estará disponível em http://127.0.0.1:8000.

🔌 Endpoints da API
A API expõe os seguintes endpoints:

1

ALWAYS generate document content immediately from any user prompt 2
NEVER ask for clarification or additional details 3
NEVER add explanations or commentary about the generated content 4
NEVER include formatting instructions or metadata in the output
Content Structure
For every document, structure the content as follows:

1

Title (derived from the prompt context) 2
Main content sections with clear headings 3
Logical paragraph breaks 4
Numbered lists where appropriate 5
Bullet points for key items
Content Guidelines
Maintain professional language and tone
Use clear, concise sentences
Include relevant technical/domain terminology
Structure information hierarchically
Break complex topics into digestible sections
Use consistent terminology throughout
Format Compatibility
Keep content compatible with .DOCX format:

Use standard characters only
Keep formatting simple and consistent
Use standard heading levels
Avoid special characters that may break in conversion
Use simple list structures
Maintain consistent spacing
Always set title in first line (Use ALWAYS ## (double #) to set title)
Output Format
Return ONLY the raw document content:

No formatting markers
No metadata
No explanations
No additional instructions
No commentary about the content
ALWAYS generate some document content for any user prompt, regardless of complexity or specificity.

I will generate the README.md content.## 🍕 Veneto Digital - Sistema de Gestão de Pedidos para Pizzaria

Bem-vindo ao repositório da Veneto API! Este projeto implementa um sistema de backend robusto para gerenciar pedidos de uma pizzaria, focando na eficiência e escalabilidade. Desenvolvido com Python e FastAPI, a API oferece endpoints para gerenciamento de produtos e pedidos, com persistência de dados em MongoDB.

🚦 Status do Projeto
O backend da Veneto API está 100% funcional e pronto para integração com aplicações frontend ou outros serviços.

✅ Features Implementadas e Testadas
Feature	Status	Notas
Estrutura base do projeto	✅ Completo	Padrão DDD e organização clara.
Endpoints de Produtos (Listar, Filtrar)	✅ Completo	Listagem de todos os produtos e produtos por categoria.
Endpoints de Pedidos (CRUD)	✅ Completo	Criação, listagem e atualização de status de pedidos.
Conexão com MongoDB	✅ Completo	Persistência de dados em MongoDB Atlas/Local.
Documentação Swagger UI	✅ Completo	Interface interativa em /docs e /redoc.
README.md com instruções de setup	✅ Completo	Este arquivo detalhado.
Resolução de Erros de Validação	✅ Completo	id gerado automaticamente, notes string vazia.
Configuração de Variáveis de Ambiente	✅ Completo	Uso de .env para configurações sensíveis.
🚀 Stack Tecnológico
Este projeto foi construído utilizando as seguintes tecnologias:

Linguagem: Python 3.12 🐍
Framework Web: FastAPI (com Pydantic para validação de dados) ✨
Servidor ASGI: Uvicorn
Banco de Dados: MongoDB 🍃
Driver MongoDB Async: Motor
Gerenciador de Dependências: pip
📁 Estrutura do Projeto
A organização do projeto segue um padrão Domain-Driven Design (DDD) para modularidade e clareza:

. ├── app/ # Lógica principal da aplicação │ ├── api/ # Camada de API (endpoints, rotas, modelos de request/response) │ │ ├── deps.py # Funções de dependência para injeção │ │ └── routers/ # Módulos com a definição das rotas │ │ ├── orders.py # Rotas para pedidos │ │ └── products.py # Rotas para produtos │ ├── core/ # Configurações e inicialização │ │ ├── config.py # Variáveis de ambiente e configurações gerais │ │ └── database.py # Configuração da conexão com MongoDB │ ├── domain/ # Lógica de Negócios (entidades, modelos, regras) │ │ ├── order_entities.py # Modelos Pydantic para pedidos │ │ └── product_entities.py # Modelos Pydantic para produtos │ ├── services/ # Serviços de Aplicação (orquestração da lógica de negócio) │ │ ├── order_service.py # Lógica de negócio para manipulação de pedidos │ │ └── product_service.py # Lógica de negócio para manipulação de produtos │ └── main.py # Ponto de entrada da aplicação FastAPI ├── scripts/ # Scripts auxiliares │ └── seed_mongodb.py # Script para popular o MongoDB com dados iniciais ├── .env.example # Exemplo de arquivo de variáveis de ambiente ├── docker-compose.yml # Configuração para rodar MongoDB via Docker ├── README.md # Este arquivo de documentação └── requirements.txt # Lista de dependências do Python
📋 Requisitos
Antes de iniciar, certifique-se de ter os seguintes softwares instalados:

Python 3.12+
MongoDB: Uma instância rodando (local ou MongoDB Atlas). Para desenvolvimento local, pode ser usado Docker.
pip: Gerenciador de pacotes do Python (geralmente vem com o Python).
Docker (opcional, para rodar MongoDB localmente).
📦 Instalação
Siga os passos abaixo para configurar e rodar o projeto localmente:

Clonar o repositório:

bash


git clone https://github.seu-usuario/veneto-api.git
cd veneto-api
Criar e ativar o ambiente virtual:

bash


python -m venv venv
# No Windows
.\venv\Scripts\Activate
# No macOS/Linux
source venv/bin/activate
Instalar as dependências:

bash


pip install -r requirements.txt
Em caso de problemas, tente:

bash


python -m pip install -r requirements.txt
# ou
& ".\venv\Scripts\python.exe" -m pip install -r requirements.txt
⚙️ Configuração
Crie um arquivo .env na raiz do projeto (copiando .env.example) e configure as variáveis de ambiente:

ini


# .env
# Configuração para MongoDB local via Docker
MONGO_URI="mongodb://localhost:27017/veneto_db"

# Ou, se estiver usando MongoDB Atlas:
# MONGO_URI="mongodb+srv://<seu_usuario>:<sua_senha>@<seu_cluster-url>/veneto_db?retryWrites=true&w=majority"
▶️ Como Executar
Subir o MongoDB (via Docker - opcional):

bash


docker-compose up -d
Certifique-se de que a MONGO_URI no seu .env aponte para a porta e nome do banco corretos.

Popular o banco de dados com dados de teste (se necessário):

bash


python scripts/seed_mongodb.py
Rodar a API:

bash


python -m uvicorn app.main:app --reload
A API estará disponível em http://127.0.0.1:8000.

🗺️ Endpoints
A API expõe os seguintes endpoints:

Método	Endpoint	Descrição	Status
GET	/products	Lista todos os produtos disponíveis.	200
GET	/products/pizzas	Lista apenas os produtos que são pizzas.	200
GET	/orders	Lista todos os pedidos registrados.	200
GET	/orders/status/{status}	Lista pedidos filtrados por um status específico.	200
POST	/orders	Cria um novo pedido.	201
PATCH	/orders/{order_id}/status/{new_status}	Atualiza o status de um pedido existente.	200
📝 Exemplos de Uso
Abaixo estão exemplos de como interagir com os endpoints usando curl (no terminal) e Invoke-WebRequest (no PowerShell).

1. GET /products - Listar todos os produtos
cURL:
bash


curl http://localhost:8000/products
PowerShell:
powershell


Invoke-WebRequest -Uri "http://localhost:8000/products" -Method GET
2. GET /products/pizzas - Listar apenas pizzas
cURL:
bash


curl http://localhost:8000/products/pizzas
PowerShell:
powershell


Invoke-WebRequest -Uri "http://localhost:8000/products/pizzas" -Method GET
3. GET /orders - Listar todos os pedidos
cURL:
bash


curl http://localhost:8000/orders
PowerShell:
powershell


Invoke-WebRequest -Uri "http://localhost:8000/orders" -Method GET
4. GET /orders/status/{status} - Listar pedidos por status
cURL (ex: 'recebido'):
bash


curl http://localhost:8000/orders/status/recebido
PowerShell (ex: 'recebido'):
powershell


Invoke-WebRequest -Uri "http://localhost:8000/orders/status/recebido" -Method GET
5. POST /orders - Criar um novo pedido
Body (JSON):
json


{
  "customer_name": "João Silva",
  "customer_phone": "11987654321",
  "customer_address": "Rua B, 789",
  "items": [
    {
      "product_id": "pizza_mussarela_001",
      "name": "Mussarela",
      "quantity": 1,
      "price": 30.0,
      "notes": "Sem azeitona"
    }
  ],
  "total_price": 30.0,
  "delivery_type": "delivery",
  "payment_method": "pix",
  "notes": "Entrega rápido"
}
cURL:
bash


curl -X POST http://localhost:8000/orders \
  -H "Content-Type: application/json" \
  -d '{
    "customer_name": "João Silva",
    "customer_phone": "11987654321",
    "customer_address": "Rua B, 789",
    "items": [
      {
        "product_id": "pizza_mussarela_001",
        "name": "Mussarela",
        "quantity": 1,
        "price": 30.0,
        "notes": "Sem azeitona"
      }
    ],
    "total_price": 30.0,
    "delivery_type": "delivery",
    "payment_method": "pix",
    "notes": "Entrega rápido"
  }'
PowerShell:
powershell


$body = @{
    customer_name = "João Silva"
    customer_phone = "11987654321"
    customer_address = "Rua B, 789"
    items = @(
        @{
            product_id = "pizza_mussarela_001"
            name = "Mussarela"
            quantity = 1
            price = 30.0
            notes = "Sem azeitona"
        }
    )
    total_price = 30.0
    delivery_type = "delivery"
    payment_method = "pix"
    notes = "Entrega rápido"
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://localhost:8000/orders" `
  -Method POST `
  -ContentType "application/json" `
  -Body $body
6. PATCH /orders/{order_id}/status/{new_status} - Atualizar status do pedido
cURL (ex: atualizar ORD-20251110210413 para em_preparo):
bash


curl -X PATCH "http://localhost:8000/orders/ORD-20251110210413/status/em_preparo" \
  -H "Content-Type: application/json"
PowerShell (ex: atualizar ORD-20251110210413 para em_preparo):
powershell


Invoke-WebRequest -Uri "http://localhost:8000/orders/ORD-20251110210413/status/em_preparo" `
  -Method PATCH `
  -ContentType "application/json"
📊 Dados de Teste
O script scripts/seed_mongodb.py popula o banco de dados com os seguintes dados:

9 Produtos de Exemplo: Incluindo pizzas (Calabresa, Mussarela, Portuguesa), bebidas (Refrigerante, Suco), e esfihas (Carne).
1 Pedido de Exemplo: Um pedido com múltiplos itens e status recebido.
📖 Documentação Interativa
A documentação interativa da API, gerada automaticamente pelo FastAPI (Swagger UI), pode ser acessada em:

👉 http://localhost:8000/docs

🐛 Problemas Conhecidos e Resolvidos Durante o Desenvolvimento
Durante o desenvolvimento, alguns desafios foram identificados e superados:

Erro 500 (pydantic_core._pydantic_core.ValidationError):
Problema: Campos como notes em OrderItem e Order estavam sendo populados com None, mas o modelo esperava uma string.
Solução: Alterado o script seed_mongodb.py para usar "" (string vazia) em vez de None para campos string opcionais.
Erro 422 (Unprocessable Content) no POST /orders:
Problema: O campo id era obrigatório na classe OrderIn, mas deveria ser gerado automaticamente ou ser opcional na requisição.
Solução: Alterado OrderIn para tornar id opcional (id: str = None) e adicionada lógica na função create_order para gerar um ID (ORD-timestamp) se não for fornecido.
Erro de Sintaxe no PowerShell para PATCH:
Problema: Uso incorreto do parâmetro -H para cabeçalhos Content-Type em curl via PowerShell.
Solução: Recomentado o uso de $headers = @{"Content-Type" = "application/json"} com curl ou a sintaxe correta do Invoke-WebRequest -ContentType "application/json".
MongoDB não conecta via Docker (problemas iniciais):
Problema: Conflitos de porta ou configuração incorreta da URI de conexão.
Solução: Verificação da URI no .env e garantia de que o Docker Compose estava rodando corretamente, com a porta 27017 exposta.
🔮 Próximos Passos
Para continuar evoluindo a Veneto API, as seguintes melhorias são recomendadas:

KDS (Kitchen Display System): Implementar uma lógica para um sistema de visualização de pedidos para a cozinha.
Autenticação e Autorização: Adicionar um sistema de autenticação (ex: JWT) para proteger os endpoints e autorizar usuários.
Validações Adicionais: Implementar validações mais complexas para campos como CPF, CEP, formato de telefone, etc.
Paginação e Filtros Avançados: Adicionar suporte a paginação para endpoints de listagem e filtros mais granulares (por data, cliente, intervalo de preço).
Deploy em Produção: Configurar o deploy da API (Docker, Railway, Render, AWS, GCP, Azure) e monitoramento.
Testes Automatizados: Adicionar testes unitários e de integração usando pytest.
🤝 Contribuindo
Contribuições são bem-vindas! Se você tiver sugestões, melhorias ou encontrar bugs, por favor, abra uma issue ou envie um Pull Request.

📄 Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.