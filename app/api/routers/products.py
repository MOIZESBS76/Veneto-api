from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel, Field, field_validator
from typing import Optional
from app.api.deps import get_product_service
from app.services.product_service import ProductService
from app.domain.entities import Product, ProductCategory, Pizza, PizzaSize
import re

router = APIRouter(prefix="/products", tags=["products"])

class PizzaSizeIn(BaseModel):
    size_cm: int = Field(..., gt=0, description="Tamanho da pizza em cm")
    price: float = Field(..., gt=0, description="Preço para este tamanho")

    @field_validator('size_cm')
    @classmethod
    def validate_size_cm(cls, v):
        if v < 20 or v > 100:
            raise ValueError('Tamanho deve estar entre 20cm e 100cm')
        return v

    @field_validator('price')
    @classmethod
    def validate_price(cls, v):
        if v <= 0:
            raise ValueError('Preço deve ser positivo')
        return round(v, 2)

class ProductIn(BaseModel):
    id: str = Field(..., min_length=1)
    name: str = Field(..., min_length=1, max_length=100)
    category: ProductCategory
    description: Optional[str] = Field(None, max_length=500)
    price: float = Field(..., gt=0, description="Preço deve ser positivo")
    image_url: Optional[str] = None

    @field_validator('price')
    @classmethod
    def validate_price(cls, v):
        return round(v, 2)

    @field_validator('image_url')
    @classmethod
    def validate_image_url(cls, v):
        if v is None:
            return v
        if not re.match(r'^https?://', v):
            raise ValueError('URL da imagem deve começar com http:// ou https://')
        return v

class PizzaIn(BaseModel):
    id: str = Field(..., min_length=1)
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    price: float = Field(..., gt=0, description="Preço base da pizza")
    image_url: Optional[str] = None
    sizes: list[PizzaSizeIn] = Field(..., min_length=1, description="Pelo menos um tamanho é obrigatório")

    @field_validator('price')
    @classmethod
    def validate_price(cls, v):
        return round(v, 2)

    @field_validator('image_url')
    @classmethod
    def validate_image_url(cls, v):
        if v is None:
            return v
        if not re.match(r'^https?://', v):
            raise ValueError('URL da imagem deve começar com http:// ou https://')
        return v

class ProductOut(BaseModel):
    id: str
    name: str
    category: ProductCategory
    description: Optional[str] = None
    price: float
    active: bool = True
    image_url: Optional[str] = None

class PizzaOut(ProductOut):
    sizes: list[PizzaSizeIn]

# Endpoints para Produtos Gerais
@router.post("", response_model=ProductOut, status_code=201)
async def create_product(
    payload: ProductIn,
    svc: ProductService = Depends(get_product_service)
):
    """Criar um novo produto (quentinha, bebida, esfiha)"""
    try:
        p = Product(**payload.model_dump())
        created = await svc.create(p)
        return ProductOut(**created.model_dump())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro ao criar produto")

@router.get("", response_model=list[ProductOut])
async def list_products(
    svc: ProductService = Depends(get_product_service),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100)
):
    """Listar todos os produtos ativos"""
    try:
        items = await svc.list_active(skip=skip, limit=limit)
        return [ProductOut(**i.model_dump()) for i in items]
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro ao listar produtos")

@router.get("/category/{category}", response_model=list[ProductOut])
async def list_by_category(
    category: ProductCategory,
    svc: ProductService = Depends(get_product_service),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100)
):
    """Listar produtos por categoria (exceto pizzas)"""
    if category == ProductCategory.PIZZA:
        raise HTTPException(
            status_code=400,
            detail="Use o endpoint /pizzas para listar pizzas"
        )
    try:
        items = await svc.list_by_category(category, skip=skip, limit=limit)
        return [ProductOut(**i.model_dump()) for i in items]
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro ao listar produtos")

# Endpoints Específicos para Pizzas
@router.post("/pizzas", response_model=PizzaOut, status_code=201)
async def create_pizza(
    payload: PizzaIn,
    svc: ProductService = Depends(get_product_service)
):
    """Criar uma nova pizza com tamanhos e preços específicos"""
    try:
        sizes = [PizzaSize(**s.model_dump()) for s in payload.sizes]
        pizza = Pizza(
            id=payload.id,
            name=payload.name,
            category=ProductCategory.PIZZA,
            description=payload.description,
            price=payload.price,
            image_url=payload.image_url,
            sizes=sizes
        )
        created = await svc.create(pizza)
        return PizzaOut(**created.model_dump())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro ao criar pizza")

@router.get("/pizzas", response_model=list[PizzaOut])
async def list_pizzas(
    svc: ProductService = Depends(get_product_service),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100)
):
    """Listar todas as pizzas com seus tamanhos e preços"""
    try:
        items = await svc.list_by_category(ProductCategory.PIZZA, skip=skip, limit=limit)
        return [PizzaOut(**i.model_dump()) for i in items]
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro ao listar pizzas")

@router.get("/pizzas/{pizza_id}", response_model=PizzaOut)
async def get_pizza(
    pizza_id: str,
    svc: ProductService = Depends(get_product_service)
):
    """Obter detalhes de uma pizza específica com seus tamanhos"""
    try:
        item = await svc.get_by_id(pizza_id)
        if not item or item.category != ProductCategory.PIZZA:
            raise HTTPException(status_code=404, detail="Pizza não encontrada")
        return PizzaOut(**item.model_dump())
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro ao obter pizza")