# Scripts de Inicialização - MongoDB Veneto

## 📁 Estrutura

- `init_mongodb.js` - Script JavaScript para mongosh
- `seed_mongodb.py` - Script Python para população com async

---

## 🚀 Como usar

### Opção 1: Usar o script JavaScript (mongosh)

**Pré-requisito:**
- MongoDB instalado e rodando
- mongosh instalado

**Executar:**
```bash
# De qualquer diretório
mongosh < scripts/init_mongodb.js

# Ou dentro do mongosh
mongosh
> load("scripts/init_mongodb.js")