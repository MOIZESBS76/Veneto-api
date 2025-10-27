from typing import Optional, List, Protocol
from app.domain.entities import Product, ProductCategory
from app.domain.order_entities import Order, OrderStatus
from datetime import datetime

class ProductRepo(Protocol):
    async def by_id(self, pid: str) -> Optional[Product]: ...
    async def save(self, p: Product) -> None: ...
    async def list_by_category(self, cat: ProductCategory) -> List[Product]: ...
    async def list_active(self) -> List[Product]: ...

class MongoProductRepo:
    def __init__(self, col):
        self.col = col

    async def by_id(self, pid: str) -> Optional[Product]:
        doc = await self.col.find_one({"_id": pid})
        if not doc:
            return None
        return Product(
            id=doc["_id"],
            name=doc["name"],
            category=doc["category"],
            description=doc.get("description"),
            active=doc.get("active", True),
            image_url=doc.get("image_url")
        )

    async def save(self, p: Product) -> None:
        await self.col.update_one(
            {"_id": p.id},
            {"$set": p.dict()},
            upsert=True
        )

    async def list_by_category(self, cat: ProductCategory) -> List[Product]:
        cur = self.col.find({"category": cat.value, "active": True})
        items = []
        async for d in cur:
            items.append(Product(
                id=d["_id"],
                name=d["name"],
                category=d["category"],
                description=d.get("description"),
                active=d.get("active", True),
                image_url=d.get("image_url")
            ))
        return items

    async def list_active(self) -> List[Product]:
        cur = self.col.find({"active": True})
        items = []
        async for d in cur:
            items.append(Product(
                id=d["_id"],
                name=d["name"],
                category=d["category"],
                description=d.get("description"),
                active=d.get("active", True),
                image_url=d.get("image_url")
            ))
        return items
    

class OrderRepo(Protocol):
    async def by_id(self, oid: str) -> Optional[Order]: ...
    async def save(self, o: Order) -> None: ...
    async def list_by_status(self, status: OrderStatus) -> List[Order]: ...
    async def list_all(self) -> List[Order]: ...
    async def update_status(self, oid: str, status: OrderStatus) -> None: ...

class MongoOrderRepo:
    def __init__(self, col):
        self.col = col

    async def by_id(self, oid: str) -> Optional[Order]:
        doc = await self.col.find_one({"_id": oid})
        if not doc:
            return None
        return Order(**doc)

    async def save(self, o: Order) -> None:
        await self.col.update_one(
            {"_id": o.id},
            {"$set": o.dict()},
            upsert=True
        )

    async def list_by_status(self, status: OrderStatus) -> List[Order]:
        cur = self.col.find({"status": status.value})
        items = []
        async for d in cur:
            items.append(Order(**d))
        return items

    async def list_all(self) -> List[Order]:
        cur = self.col.find({})
        items = []
        async for d in cur:
            items.append(Order(**d))
        return items

    async def update_status(self, oid: str, status: OrderStatus) -> None:
        await self.col.update_one(
            {"_id": oid},
            {"$set": {"status": status.value, "updated_at": datetime.utcnow()}}
        )
    
