# Status do Projeto Veneto Digital

## Completo
- Estrutura base do projeto
- Endpoints de Produtos (CRUD)
- Endpoints de Pedidos (CRUD)
- Documentação Swagger UI
- README.md com instruções de setup

## Em Progresso
- Conexão com MongoDB (problemas com Motor/async)
- Testes automatizados

## Não Iniciado
- KDS (Kitchen Display System)
- Integração de Pagamentos
- Painel Admin

## Problemas Conhecidos
- MongoDB não conecta via Docker (usar localhost ou Atlas)
- Necessário refatorar para Beanie ou usar MongoDB local

## Próximos Passos
1. Resolver problema de MongoDB
2. Implementar KDS
3. Adicionar testes com pytest
4. Integração de pagamentos


## Para voltar para o projeto
# Clonar o projeto
git clone https://github.com/seu-usuario/veneto-api.git
cd veneto-api

# Ativar venv
.\venv\Scripts\Activate

# Instalar dependências
pip install -r requirements.txt
Em caso de problemas
python -m pip install -r requirements.txt
ou
& ".\venv\Scripts\python.exe" -m pip install -r requirements.txt

# Subir MongoDB
docker-compose up -d

# Rodar a API
python -m uvicorn app.main:app --reload

## Verificar o histórico de commits

git log --oneline