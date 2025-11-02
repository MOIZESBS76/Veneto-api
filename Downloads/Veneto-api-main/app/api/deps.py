from fastapi import Depends
from app.infra.db import get_db
from app.infra.repos import MongoProductRepo
from app.services.product_service import ProductService

async def get_product_repo(db = Depends(get_db)):
    col = db["products"]
    return MongoProductRepo(col)

def get_product_service(repo = Depends(get_product_repo)):
    return ProductService(repo)

# Atualização para adicionar OrderService
from app.infra.repos import MongoOrderRepo
from app.services.order_service import OrderService

async def get_order_repo(db = Depends(get_db)):
    col = db["orders"]
    return MongoOrderRepo(col)

def get_order_service(repo = Depends(get_order_repo)):
    return OrderService(repo)