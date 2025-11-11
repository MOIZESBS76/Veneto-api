# Modelo de Banco de Dados - MongoDB Veneto API

## 📐 Modelo Lógico

### Collections (Tabelas)

#### 1. **products**
- Armazena todos os produtos (pizzas, quentinhas, bebidas, esfihas)
- Documento polimórfico (suporta pizzas com tamanhos específicos)

#### 2. **orders**
- Armazena os pedidos realizados
- Referencia produtos via ID

#### 3. **order_items**
- Items individuais de cada pedido
- Desnormalizado dentro do documento order (por performance)

---

## 🗄️ Estrutura Física das Collections

### 1. Collection: `products`

**Índices:**
```javascript
db.products.createIndex({ "category": 1, "active": 1 })
db.products.createIndex({ "active": 1 })
db.products.createIndex({ "name": 1 })