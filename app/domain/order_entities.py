from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum
from datetime import datetime

class OrderStatus(str, Enum):
    RECEBIDO = "recebido"
    EM_PREPARO = "em_preparo"
    PRONTO = "pronto"
    SAIU_ENTREGA = "saiu_entrega"
    ENTREGUE = "entregue"
    CANCELADO = "cancelado"

class OrderItem(BaseModel):
    product_id: str
    name: str
    quantity: int
    price: float
    notes: Optional[str] = None  # Observações (ex: "sem cebola")

class Order(BaseModel):
    id: str = Field(..., description="Order ID (ex: ORD-001)")
    customer_name: str
    customer_phone: str
    customer_address: Optional[str] = None
    items: List[OrderItem]
    total_price: float
    status: OrderStatus = OrderStatus.RECEBIDO
    delivery_type: str = "delivery"  # "delivery" ou "retirada"
    payment_method: str = "dinheiro"  # "dinheiro", "cartao", "pix"
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    notes: Optional[str] = None  # Observações gerais do pedido