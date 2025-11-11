"""
Script de seed (população) do MongoDB com dados de exemplo
Execute com: python scripts/seed_mongodb.py
"""

import asyncio
import sys
from datetime import datetime, timezone
from pathlib import Path

# Adicionar a raiz do projeto ao path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

# Configuração
MONGODB_URL = "mongodb://localhost:27017"
DATABASE_NAME = "veneto_db"

async def connect_db() -> AsyncIOMotorDatabase:
    """Conectar ao MongoDB"""
    client = AsyncIOMotorClient(MONGODB_URL)
    return client[DATABASE_NAME]

async def clear_collections(db: AsyncIOMotorDatabase):
    """Limpar collections existentes"""
    print("🗑️  Limpando dados existentes...")
    await db.products.delete_many({})
    await db.orders.delete_many({})
    print("✅ Collections limpas\n")

async def seed_products(db: AsyncIOMotorDatabase):
    """Inserir produtos de exemplo"""
    print("📝 Inserindo produtos de exemplo...\n")
    
    products_data = [
        # Pizzas
        {
            "_id": "pizza_calabresa_001",
            "name": "Calabresa",
            "category": "pizza",
            "description": "Calabresa com queijo derretido",
            "price": 25.00,
            "active": True,
            "image_url": "https://example.com/calabresa.jpg",
            "sizes": [
                {"size_cm": 35, "price": 25.00},
                {"size_cm": 45, "price": 35.00},
                {"size_cm": 55, "price": 45.00}
            ],
            "created_at": datetime.now(timezone.utc)
        },
        {
            "_id": "pizza_mussarela_001",
            "name": "Mussarela",
            "category": "pizza",
            "description": "Mussarela fresca com tomate",
            "price": 20.00,
            "active": True,
            "image_url": "https://example.com/mussarela.jpg",
            "sizes": [
                {"size_cm": 35, "price": 20.00},
                {"size_cm": 45, "price": 30.00},
                {"size_cm": 55, "price": 40.00}
            ],
            "created_at": datetime.now(timezone.utc)
        },
        {
            "_id": "pizza_portuguesa_001",
            "name": "Portuguesa",
            "category": "pizza",
            "description": "Presunto, ovo, cebola e azeitona",
            "price": 28.00,
            "active": True,
            "image_url": "https://example.com/portuguesa.jpg",
            "sizes": [
                {"size_cm": 35, "price": 28.00},
                {"size_cm": 45, "price": 38.00},
                {"size_cm": 55, "price": 48.00}
            ],
            "created_at": datetime.now(timezone.utc)
        },
        # Quentinhas
        {
            "_id": "quentinha_frango_001",
            "name": "Frango com Arroz",
            "category": "quentinha",
            "description": "Frango grelhado com arroz integral",
            "price": 15.00,
            "active": True,
            "image_url": "https://example.com/frango.jpg",
            "created_at": datetime.now(timezone.utc)
        },
        {
            "_id": "quentinha_carne_001",
            "name": "Carne com Batata",
            "category": "quentinha",
            "description": "Carne assada com batata doce",
            "price": 18.00,
            "active": True,
            "image_url": "https://example.com/carne.jpg",
            "created_at": datetime.now(timezone.utc)
        },
        # Bebidas
        {
            "_id": "bebida_refri_2l",
            "name": "Refrigerante 2L",
            "category": "bebida",
            "description": "Refrigerante 2 litros",
            "price": 8.50,
            "active": True,
            "image_url": "https://example.com/refri.jpg",
            "created_at": datetime.now(timezone.utc)
        },
        {
            "_id": "bebida_suco_500ml",
            "name": "Suco Natural 500ml",
            "category": "bebida",
            "description": "Suco natural de frutas",
            "price": 6.00,
            "active": True,
            "image_url": "https://example.com/suco.jpg",
            "created_at": datetime.now(timezone.utc)
        },
        # Esfihas
        {
            "_id": "esfiha_carne_001",
            "name": "Esfiha de Carne",
            "category": "esfiha",
            "description": "Esfiha recheada com carne",
            "price": 5.00,
            "active": True,
            "image_url": "https://example.com/esfiha_carne.jpg",
            "created_at": datetime.now(timezone.utc)
        },
        {
            "_id": "esfiha_queijo_001",
            "name": "Esfiha de Queijo",
            "category": "esfiha",
            "description": "Esfiha recheada com queijo derretido",
            "price": 4.50,
            "active": True,
            "image_url": "https://example.com/esfiha_queijo.jpg",
            "created_at": datetime.now(timezone.utc)
        }
    ]
    
    result = await db.products.insert_many(products_data)
    print(f"✅ {len(result.inserted_ids)} produtos inseridos\n")

async def seed_orders(db: AsyncIOMotorDatabase):
    """Inserir pedido de exemplo"""
    print("📋 Inserindo pedido de exemplo...\n")
    
    order_data = {
        "_id": "order_20250101_001",
        "id": "ORD-001",
        "customer_name": "Maria Santos",
        "customer_phone": "(11) 99999-8888",
        "customer_address": "Av. Principal, 456, São Paulo, SP",
        "items": [
            {
                "product_id": "pizza_calabresa_001",
                "name": "Calabresa",
                "quantity": 1,
                "price": 35.00,
                "notes": "Bem passada"
            },
            {
                "product_id": "bebida_refri_2l",
                "name": "Refrigerante 2L",
                "quantity": 2,
                "price": 8.50,
                "notes": ""
            },
            {
                "product_id": "esfiha_carne_001",
                "name": "Esfiha de Carne",
                "quantity": 4,
                "price": 5.00,
                "notes": ""
            }
        ],
        "total_price": 85.50,
        "status": "recebido",
        "delivery_type": "delivery",
        "payment_method": "dinheiro",
        "created_at": datetime.now(timezone.utc),
        "updated_at": datetime.now(timezone.utc),
        "notes": "Sem cebola na pizza"
    }
    
    result = await db.orders.insert_one(order_data)
    print(f"✅ Pedido inserido: {order_data['id']}\n")

async def show_statistics(db: AsyncIOMotorDatabase):
    """Exibir estatísticas"""
    print("📊 Estatísticas do banco:\n")
    
    products_count = await db.products.count_documents({})
    pizzas_count = await db.products.count_documents({"category": "pizza"})
    orders_count = await db.orders.count_documents({})
    
    print(f"  • Total de produtos: {products_count}")
    print(f"  • Total de pizzas: {pizzas_count}")
    print(f"  • Total de pedidos: {orders_count}\n")

async def main():
    """Função principal"""
    print("\n" + "="*70)
    print("🌱 Seed MongoDB - Veneto API")
    print("="*70 + "\n")
    
    try:
        # Conectar
        db = await connect_db()
        print("✅ Conectado ao MongoDB\n")
        
        # Limpar
        await clear_collections(db)
        
        # Popular
        await seed_products(db)
        await seed_orders(db)
        
        # Estatísticas
        await show_statistics(db)
        
        print("="*70)
        print("✅ SEED CONCLUÍDO COM SUCESSO!")
        print("="*70 + "\n")
        
    except Exception as e:
        print(f"❌ Erro: {e}\n")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())