// ============================================================================
// Script de Inicialização do MongoDB - Veneto API
// ============================================================================
// Execute com: mongosh < init_mongodb.js
// Ou dentro do mongosh: load("init_mongodb.js")
// ============================================================================

// Selecionar banco de dados
use veneto_db;

console.log("🔧 Inicializando banco de dados Veneto...\n");

// ============================================================================
// 1. CRIAR COLLECTIONS COM VALIDAÇÃO
// ============================================================================

console.log("📦 Criando collection 'products'...");
db.createCollection("products", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["_id", "name", "category", "price", "active"],
      properties: {
        _id: { 
          bsonType: "string",
          description: "ID único do produto"
        },
        name: { 
          bsonType: "string",
          minLength: 1,
          maxLength: 100,
          description: "Nome do produto"
        },
        category: { 
          enum: ["pizza", "quentinha", "bebida", "esfiha"],
          description: "Categoria do produto"
        },
        description: { 
          bsonType: "string",
          maxLength: 500
        },
        price: { 
          bsonType: "double",
          minimum: 0.01,
          description: "Preço base do produto"
        },
        active: { 
          bsonType: "bool",
          description: "Produto ativo ou inativo"
        },
        image_url: { 
          bsonType: "string"
        },
        sizes: {
          bsonType: "array",
          description: "Tamanhos disponíveis (apenas para pizzas)",
          items: {
            bsonType: "object",
            required: ["size_cm", "price"],
            properties: {
              size_cm: { 
                bsonType: "int",
                minimum: 20,
                maximum: 100
              },
              price: { 
                bsonType: "double",
                minimum: 0.01
              }
            }
          }
        },
        created_at: { 
          bsonType: "date"
        },
        updated_at: {
          bsonType: "date"
        }
      }
    }
  }
});
console.log("✅ Collection 'products' criada\n");

console.log("📦 Criando collection 'orders'...");
db.createCollection("orders", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["_id", "status", "customer_name", "total_price", "items"],
      properties: {
        _id: { 
          bsonType: "string",
          description: "ID único do pedido"
        },
        status: { 
          enum: ["pending", "preparing", "ready", "delivered", "cancelled"],
          description: "Status do pedido"
        },
        customer_name: { 
          bsonType: "string",
          minLength: 1,
          maxLength: 100
        },
        customer_phone: { 
          bsonType: "string"
        },
        delivery_address: { 
          bsonType: "string"
        },
        total_price: { 
          bsonType: "double",
          minimum: 0.01
        },
        items: { 
          bsonType: "array",
          minItems: 1,
          items: {
            bsonType: "object",
            required: ["product_id", "product_name", "quantity", "unit_price"],
            properties: {
              product_id: { bsonType: "string" },
              product_name: { bsonType: "string" },
              quantity: { bsonType: "int", minimum: 1 },
              size_cm: { bsonType: "int" },
              unit_price: { bsonType: "double", minimum: 0.01 },
              subtotal: { bsonType: "double", minimum: 0.01 }
            }
          }
        },
        notes: { 
          bsonType: "string"
        },
        created_at: { 
          bsonType: "date"
        },
        updated_at: { 
          bsonType: "date"
        },
        estimated_time_minutes: {
          bsonType: "int",
          minimum: 5
        }
      }
    }
  }
});
console.log("✅ Collection 'orders' criada\n");

// ============================================================================
// 2. CRIAR ÍNDICES
// ============================================================================

console.log("🔍 Criando índices...\n");

// Índices para products
console.log("  • Índice: products (category, active)");
db.products.createIndex({ "category": 1, "active": 1 });

console.log("  • Índice: products (active)");
db.products.createIndex({ "active": 1 });

console.log("  • Índice: products (name)");
db.products.createIndex({ "name": 1 });

// Índices para orders
console.log("  • Índice: orders (status)");
db.orders.createIndex({ "status": 1 });

console.log("  • Índice: orders (created_at)");
db.orders.createIndex({ "created_at": -1 });

console.log("  • Índice: orders (status, created_at)");
db.orders.createIndex({ "status": 1, "created_at": -1 });

console.log("\n✅ Índices criados\n");

// ============================================================================
// 3. INSERIR DADOS DE EXEMPLO
// ============================================================================

console.log("📝 Inserindo dados de exemplo...\n");

// Pizzas
console.log("  • Inserindo pizzas...");
db.products.insertMany([
  {
    "_id": "pizza_calabresa_001",
    "name": "Calabresa",
    "category": "pizza",
    "description": "Calabresa com queijo derretido",
    "price": 25.00,
    "active": true,
    "image_url": "https://example.com/calabresa.jpg",
    "sizes": [
      { "size_cm": 35, "price": 25.00 },
      { "size_cm": 45, "price": 35.00 },
      { "size_cm": 55, "price": 45.00 }
    ],
    "created_at": new Date(),
    "updated_at": new Date()
  },
  {
    "_id": "pizza_mussarela_001",
    "name": "Mussarela",
    "category": "pizza",
    "description": "Mussarela fresca com tomate",
    "price": 20.00,
    "active": true,
    "image_url": "https://example.com/mussarela.jpg",
    "sizes": [
      { "size_cm": 35, "price": 20.00 },
      { "size_cm": 45, "price": 30.00 },
      { "size_cm": 55, "price": 40.00 }
    ],
    "created_at": new Date(),
    "updated_at": new Date()
  },
  {
    "_id": "pizza_portuguesa_001",
    "name": "Portuguesa",
    "category": "pizza",
    "description": "Presunto, ovo, cebola e azeitona",
    "price": 28.00,
    "active": true,
    "image_url": "https://example.com/portuguesa.jpg",
    "sizes": [
      { "size_cm": 35, "price": 28.00 },
      { "size_cm": 45, "price": 38.00 },
      { "size_cm": 55, "price": 48.00 }
    ],
    "created_at": new Date(),
    "updated_at": new Date()
  }
]);

// Quentinhas
console.log("  • Inserindo quentinhas...");
db.products.insertMany([
  {
    "_id": "quentinha_frango_001",
    "name": "Frango com Arroz",
    "category": "quentinha",
    "description": "Frango grelhado com arroz integral",
    "price": 15.00,
    "active": true,
    "image_url": "https://example.com/frango.jpg",
    "created_at": new Date(),
    "updated_at": new Date()
  },
  {
    "_id": "quentinha_carne_001",
    "name": "Carne com Batata",
    "category": "quentinha",
    "description": "Carne assada com batata doce",
    "price": 18.00,
    "active": true,
    "image_url": "https://example.com/carne.jpg",
    "created_at": new Date(),
    "updated_at": new Date()
  }
]);

// Bebidas
console.log("  • Inserindo bebidas...");
db.products.insertMany([
  {
    "_id": "bebida_refri_2l",
    "name": "Refrigerante 2L",
    "category": "bebida",
    "description": "Refrigerante 2 litros",
    "price": 8.50,
    "active": true,
    "image_url": "https://example.com/refri.jpg",
    "created_at": new Date(),
    "updated_at": new Date()
  },
  {
    "_id": "bebida_suco_500ml",
    "name": "Suco Natural 500ml",
    "category": "bebida",
    "description": "Suco natural de frutas",
    "price": 6.00,
    "active": true,
    "image_url": "https://example.com/suco.jpg",
    "created_at": new Date(),
    "updated_at": new Date()
  }
]);

// Esfihas
console.log("  • Inserindo esfihas...");
db.products.insertMany([
  {
    "_id": "esfiha_carne_001",
    "name": "Esfiha de Carne",
    "category": "esfiha",
    "description": "Esfiha recheada com carne",
    "price": 5.00,
    "active": true,
    "image_url": "https://example.com/esfiha_carne.jpg",
    "created_at": new Date(),
    "updated_at": new Date()
  },
  {
    "_id": "esfiha_queijo_001",
    "name": "Esfiha de Queijo",
    "category": "esfiha",
    "description": "Esfiha recheada com queijo derretido",
    "price": 4.50,
    "active": true,
    "image_url": "https://example.com/esfiha_queijo.jpg",
    "created_at": new Date(),
    "updated_at": new Date()
  }
]);

console.log("\n✅ Dados de exemplo inseridos\n");

// ============================================================================
// 4. INSERIR PEDIDO DE EXEMPLO
// ============================================================================

console.log("📋 Inserindo pedido de exemplo...");
db.orders.insertOne({
  "_id": "order_20250101_001",
  "status": "pending",
  "customer_name": "Maria Santos",
  "customer_phone": "(11) 99999-8888",
  "delivery_address": "Av. Principal, 456, São Paulo, SP",
  "total_price": 85.50,
  "items": [
    {
      "product_id": "pizza_calabresa_001",
      "product_name": "Calabresa",
      "quantity": 1,
      "size_cm": 45,
      "unit_price": 35.00,
      "subtotal": 35.00
    },
    {
      "product_id": "bebida_refri_2l",
      "product_name": "Refrigerante 2L",
      "quantity": 2,
      "unit_price": 8.50,
      "subtotal": 17.00
    },
    {
      "product_id": "esfiha_carne_001",
      "product_name": "Esfiha de Carne",
      "quantity": 4,
      "unit_price": 5.00,
      "subtotal": 20.00
    }
  ],
  "notes": "Sem cebola na pizza, bem passada",
  "created_at": new Date(),
  "updated_at": new Date(),
  "estimated_time_minutes": 45
});

console.log("✅ Pedido de exemplo inserido\n");

// ============================================================================
// 5. EXIBIR ESTATÍSTICAS
// ============================================================================

console.log("📊 Estatísticas do banco:\n");

const productsCount = db.products.countDocuments();
const pizzasCount = db.products.countDocuments({ category: "pizza" });
const ordersCount = db.orders.countDocuments();

console.log(`  • Total de produtos: ${productsCount}`);
console.log(`  • Total de pizzas: ${pizzasCount}`);
console.log(`  • Total de pedidos: ${ordersCount}`);

console.log("\n" + "=".repeat(70));
console.log("✅ INICIALIZAÇÃO CONCLUÍDA COM SUCESSO!");
console.log("=".repeat(70) + "\n");

console.log("📍 Próximos passos:");
console.log("  1. Verificar dados: db.products.find()");
console.log("  2. Verificar pedidos: db.orders.find()");
console.log("  3. Conectar API: Configure a string de conexão");
console.log("  4. Testar endpoints: http://localhost:8000/docs\n");