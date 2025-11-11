"""
Script para verificar dados no MongoDB
Execute com: python scripts/check_mongodb.py
"""

import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def check():
    client = AsyncIOMotorClient('mongodb://localhost:27017')
    db = client['veneto_db']
    
    print('\n' + '='*70)
    print('📊 VERIFICAÇÃO DO MONGODB - VENETO API')
    print('='*70 + '\n')
    
    try:
        # Contar
        products = await db.products.count_documents({})
        pizzas = await db.products.count_documents({'category': 'pizza'})
        quentinhas = await db.products.count_documents({'category': 'quentinha'})
        bebidas = await db.products.count_documents({'category': 'bebida'})
        esfihas = await db.products.count_documents({'category': 'esfiha'})
        orders = await db.orders.count_documents({})
        
        print('📦 PRODUTOS:')
        print(f'  • Total: {products}')
        print(f'  • Pizzas: {pizzas}')
        print(f'  • Quentinhas: {quentinhas}')
        print(f'  • Bebidas: {bebidas}')
        print(f'  • Esfihas: {esfihas}')
        
        print(f'\n📋 PEDIDOS:')
        print(f'  • Total: {orders}\n')
        
        # Ver uma pizza com tamanhos
        pizza = await db.products.find_one({'_id': 'pizza_calabresa_001'})
        if pizza:
            print('🍕 PIZZA CALABRESA:')
            print(f'  Nome: {pizza["name"]}')
            print(f'  Descrição: {pizza["description"]}')
            print(f'  Preço base: R$ {pizza["price"]:.2f}')
            print(f'  Ativa: {"Sim" if pizza["active"] else "Não"}')
            print(f'  Tamanhos:')
            for size in pizza['sizes']:
                print(f'    - {size["size_cm"]}cm: R$ {size["price"]:.2f}')
        
        # Ver um pedido
        order = await db.orders.find_one()
        if order:
            print(f'\n📦 PEDIDO EXEMPLO:')
            print(f'  ID: {order["_id"]}')
            print(f'  Cliente: {order["customer_name"]}')
            print(f'  Status: {order["status"]}')
            print(f'  Total: R$ {order["total_price"]:.2f}')
            print(f'  Items:')
            for item in order['items']:
                print(f'    - {item["product_name"]} x{item["quantity"]}: R$ {item["subtotal"]:.2f}')
        
        print('\n' + '='*70)
        print('✅ CONEXÃO SUCESSO!')
        print('='*70 + '\n')
        
    except Exception as e:
        print(f'❌ Erro ao conectar: {e}\n')
    
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(check())