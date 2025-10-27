from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.api.deps import get_product_service
from app.services.product_service import ProductService
from app.domain.entities import Product, ProductCategory

router = APIRouter(prefix="/products", tags=["products"])

class ProductIn(BaseModel):
    id: str
    name: str
    category: ProductCategory
    description: Optional[str] = None
    price: float
    image_url: Optional[str] = None

class ProductOut(BaseModel):
    id: str
    name: str
    category: ProductCategory
    description: Optional[str] = None
    price: float
    active: bool = True
    image_url: Optional[str] = None

@router.post("", response_model=ProductOut, status_code=201)
async def create_product(payload: ProductIn, svc: ProductService = Depends(get_product_service)):
    try:
        p = Product(**payload.dict())
        created = await svc.create(p)
        return ProductOut(**created.dict())
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))

@router.get("", response_model=list[ProductOut])
async def list_products(svc: ProductService = Depends(get_product_service)):
    items = await svc.list_active()
    return [ProductOut(**i.dict()) for i in items]

@router.get("/category/{category}", response_model=list[ProductOut])
async def list_by_category(category: ProductCategory, svc: ProductService = Depends(get_product_service)):
    items = await svc.list_by_category(category)
    return [ProductOut(**i.dict()) for i in items]