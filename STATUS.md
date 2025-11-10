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

------------------------------------------------------------------------------
Próximo Passos:

Para a classe Pizza, como ela herda de Product e tem preços específicos por tamanho, você poderia:

1. Usar o campo price como preço base ou preço do menor tamanho
2. Adicionar validação para garantir que a lista de sizes não esteja vazia
3. Adicionar validação para os tamanhos de pizza

No arquivo products.py, você poderia adicionar validações adicionais:

4. Verificar se o preço é positivo
5. Validar o formato da URL da imagem
6. Adicionar endpoint específico para pizzas que lide com os diferentes tamanhos

No repositório (repos.py), seria bom adicionar:

7. Índices para melhorar a performance das consultas por categoria
8. Validação adicional antes de salvar os documentos
9. Tratamento de erros mais específico para problemas de banco de dados

