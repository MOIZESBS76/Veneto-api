from pydantic import BaseModel, Field
from typing import Optional

class Product(BaseModel):
    id: str = Field(..., description="Product ID")
    name: str
    price: float
    active: bool = True