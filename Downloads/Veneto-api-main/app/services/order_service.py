from app.domain.order_entities import Order, OrderStatus
from app.infra.repos import OrderRepo
from datetime import datetime

class OrderService:
    def __init__(self, repo: OrderRepo):
        self.repo = repo

    async def create(self, o: Order) -> Order:
        exists = await self.repo.by_id(o.id)
        if exists:
            raise ValueError("Pedido já existe")
        o.created_at = datetime.utcnow()
        o.updated_at = datetime.utcnow()
        await self.repo.save(o)
        return o

    async def list_by_status(self, status: OrderStatus) -> list[Order]:
        return await self.repo.list_by_status(status)

    async def list_all(self) -> list[Order]:
        return await self.repo.list_all()

    async def update_status(self, oid: str, status: OrderStatus) -> Order:
        await self.repo.update_status(oid, status)
        return await self.repo.by_id(oid)