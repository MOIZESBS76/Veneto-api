from typing import Protocol, Optional
from app.domain.entities import Product

class ProductRepo(Protocol):
    async def by_id(self, pid: str) -> Optional[Product]: ...
    async def save(self, p: Product) -> None: ...
    async def list_active(self) -> list[Product]: ...

class MongoProductRepo:
    def __init__(self, col):
        self.col = col

    async def by_id(self, pid: str) -> Optional[Product]:
        doc = await self.col.find_one({"_id": pid})
        return Product(id=doc["_id"], name=doc["name"], price=doc["price"], active=doc.get("active", True)) if doc else None

    async def save(self, p: Product) -> None:
        await self.col.update_one(
            {"_id": p.id},
            {"$set": {"name": p.name, "price": p.price, "active": p.active}},
            upsert=True,
        )

    async def list_active(self) -> list[Product]:
        cur = self.col.find({"active": True})
        items: list[Product] = []
        async for d in cur:
            items.append(Product(id=d["_id"], name=d["name"], price=d["price"], active=d.get("active", True)))
        return items