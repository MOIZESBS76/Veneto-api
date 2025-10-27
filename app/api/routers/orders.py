from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.api.deps import get_order_service
from app.services.order_service import OrderService
from app.domain.order_entities import Order, OrderStatus, OrderItem
from datetime import datetime

router = APIRouter(prefix="/orders", tags=["orders"])

class OrderItemIn(BaseModel):
    product_id: str
    name: str
    quantity: int
    price: float
    notes: str = None

class OrderIn(BaseModel):
    id: str
    customer_name: str
    customer_phone: str
    customer_address: str = None
    items: list[OrderItemIn]
    total_price: float
    delivery_type: str = "delivery"
    payment_method: str = "dinheiro"
    notes: str = None

class OrderOut(BaseModel):
    id: str
    customer_name: str
    customer_phone: str
    customer_address: str = None
    items: list[OrderItemIn]
    total_price: float
    status: OrderStatus
    delivery_type: str
    payment_method: str
    created_at: datetime
    updated_at: datetime
    notes: str = None

@router.post("", response_model=OrderOut, status_code=201)
async def create_order(payload: OrderIn, svc: OrderService = Depends(get_order_service)):
    try:
        items = [OrderItem(**i.dict()) for i in payload.items]
        o = Order(
            id=payload.id,
            customer_name=payload.customer_name,
            customer_phone=payload.customer_phone,
            customer_address=payload.customer_address,
            items=items,
            total_price=payload.total_price,
            delivery_type=payload.delivery_type,
            payment_method=payload.payment_method,
            notes=payload.notes
        )
        created = await svc.create(o)
        return OrderOut(**created.dict())
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))

@router.get("", response_model=list[OrderOut])
async def list_orders(svc: OrderService = Depends(get_order_service)):
    items = await svc.list_all()
    return [OrderOut(**i.dict()) for i in items]

@router.get("/status/{status}", response_model=list[OrderOut])
async def list_by_status(status: OrderStatus, svc: OrderService = Depends(get_order_service)):
    items = await svc.list_by_status(status)
    return [OrderOut(**i.dict()) for i in items]

@router.patch("/{order_id}/status/{new_status}", response_model=OrderOut)
async def update_order_status(order_id: str, new_status: OrderStatus, svc: OrderService = Depends(get_order_service)):
    try:
        updated = await svc.update_status(order_id, new_status)
        return OrderOut(**updated.dict())
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))