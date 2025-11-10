from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class ProductCategory(str, Enum):
    PIZZA = "pizza"
    QUENTINHA = "quentinha"
    BEBIDA = "bebida"
    ESFIHA = "esfiha"

class Product(BaseModel):
    id: str = Field(..., description="Product ID")
    name: str
    category: ProductCategory
    description: Optional[str] = None
    price: float = Field(..., description="Product price")
    active: bool = True
    image_url: Optional[str] = None

class PizzaSize(BaseModel):
    size_cm: int  # ex: 35, 45
    price: float

class Pizza(Product):
    sizes: list[PizzaSize] = []  # Tamanhos e preços em tela separada