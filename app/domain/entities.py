from pydantic import BaseModel, Field, field_validator
from typing import Optional
from enum import Enum
import re

class ProductCategory(str, Enum):
    PIZZA = "pizza"
    QUENTINHA = "quentinha"
    BEBIDA = "bebida"
    ESFIHA = "esfiha"

class PizzaSize(BaseModel):
    size_cm: int  # ex: 35, 45
    price: float

    @field_validator('size_cm')
    @classmethod
    def validate_size_cm(cls, v):
        if v <= 0:
            raise ValueError('Tamanho da pizza deve ser positivo')
        if v < 20 or v > 100:
            raise ValueError('Tamanho deve estar entre 20cm e 100cm')
        return v

    @field_validator('price')
    @classmethod
    def validate_price(cls, v):
        if v <= 0:
            raise ValueError('Preço deve ser positivo')
        return round(v, 2)

class Product(BaseModel):
    id: str = Field(..., description="Product ID")
    name: str = Field(..., min_length=1, max_length=100)
    category: ProductCategory
    description: Optional[str] = Field(None, max_length=500)
    price: float = Field(..., description="Product price")
    active: bool = True
    image_url: Optional[str] = None

    @field_validator('price')
    @classmethod
    def validate_price(cls, v):
        if v <= 0:
            raise ValueError('Preço deve ser positivo')
        return round(v, 2)

    @field_validator('image_url')
    @classmethod
    def validate_image_url(cls, v):
        if v is None:
            return v
        if not re.match(r'^https?://', v):
            raise ValueError('URL da imagem deve começar com http:// ou https://')
        return v

class Pizza(Product):
    sizes: list[PizzaSize] = Field(default_factory=list)

    @field_validator('sizes')
    @classmethod
    def validate_sizes(cls, v):
        if not v or len(v) == 0:
            raise ValueError('Pizza deve ter pelo menos um tamanho')
        return v

    @field_validator('price')
    @classmethod
    def validate_price(cls, v):
        if v <= 0:
            raise ValueError('Preço base deve ser positivo')
        return round(v, 2)