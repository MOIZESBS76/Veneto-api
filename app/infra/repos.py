from typing import Optional, List, Protocol, Any
from app.domain.entities import Product, ProductCategory, Pizza
from app.domain.order_entities import Order, OrderStatus
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

# ============== PRODUCT REPO ==============

class ProductRepo(Protocol):
    async def by_id(self, pid: str) -> Optional[Product]: ...
    async def save(self, p: Product) -> None: ...
    async def list_by_category(self, cat: ProductCategory, skip: int = 0, limit: int = 10) -> List[Product]: ...
    async def list_active(self, skip: int = 0, limit: int = 10) -> List[Product]: ...

class MongoProductRepo:
    def __init__(self, col: Any):
        self.col = col

    async def by_id(self, pid: str) -> Optional[Product]:
        """Obter produto por ID com tratamento de erros"""
        try:
            if not pid or len(pid.strip()) == 0:
                logger.warning("ID de produto vazio")
                return None
            
            doc = await self.col.find_one({"_id": pid})
            if not doc:
                return None
            
            return self._doc_to_product(doc)
        except Exception as e:
            logger.error(f"Erro ao buscar produto {pid}: {e}")
            raise ValueError(f"Erro ao buscar produto: {str(e)}")

    async def save(self, p: Product) -> None:
        """Salvar produto com validações e tratamento de erros"""
        try:
            # Validações
            if not p.id or len(p.id.strip()) == 0:
                raise ValueError("ID do produto é obrigatório")
            
            if not p.name or len(p.name.strip()) == 0:
                raise ValueError("Nome do produto é obrigatório")
            
            if p.price <= 0:
                raise ValueError("Preço deve ser positivo")
            
            # Validação específica para pizzas
            if isinstance(p, Pizza):
                if not p.sizes or len(p.sizes) == 0:
                    raise ValueError("Pizza deve ter pelo menos um tamanho")
            
            # Preparar documento para salvar
            doc = p.model_dump()
            doc["_id"] = p.id
            
            result = await self.col.update_one(
                {"_id": p.id},
                {"$set": doc},
                upsert=True
            )
            
            if result.upserted_id:
                logger.info(f"Produto criado: {p.id}")
            else:
                logger.info(f"Produto atualizado: {p.id}")
                
        except Exception as e:
            logger.error(f"Erro ao salvar produto {p.id}: {e}")
            raise ValueError(f"Erro ao salvar produto: {str(e)}")

    async def list_by_category(
        self,
        cat: ProductCategory,
        skip: int = 0,
        limit: int = 10
    ) -> List[Product]:
        """Listar produtos por categoria com paginação"""
        try:
            if skip < 0 or limit < 1 or limit > 100:
                raise ValueError("Parâmetros de paginação inválidos")
            
            query = {"category": cat.value, "active": True}
            cur = self.col.find(query).skip(skip).limit(limit)
            
            items = []
            async for doc in cur:
                items.append(self._doc_to_product(doc))
            
            logger.debug(f"Listados {len(items)} produtos da categoria {cat.value}")
            return items
            
        except Exception as e:
            logger.error(f"Erro ao listar produtos por categoria: {e}")
            raise ValueError(f"Erro ao listar produtos: {str(e)}")

    async def list_active(
        self,
        skip: int = 0,
        limit: int = 10
    ) -> List[Product]:
        """Listar todos os produtos ativos com paginação"""
        try:
            if skip < 0 or limit < 1 or limit > 100:
                raise ValueError("Parâmetros de paginação inválidos")
            
            cur = self.col.find({"active": True}).skip(skip).limit(limit)
            items = []
            async for doc in cur:
                items.append(self._doc_to_product(doc))
            
            logger.debug(f"Listados {len(items)} produtos ativos")
            return items
            
        except Exception as e:
            logger.error(f"Erro ao listar produtos ativos: {e}")
            raise ValueError(f"Erro ao listar produtos: {str(e)}")

    def _doc_to_product(self, doc: dict) -> Product:
        """Converter documento MongoDB para objeto Product/Pizza"""
        category = doc.get("category")
        
        # Se for pizza, retornar instância de Pizza
        if category == ProductCategory.PIZZA.value and "sizes" in doc:
            return Pizza(
                id=doc["_id"],
                name=doc["name"],
                category=category,
                description=doc.get("description"),
                price=doc.get("price", 0.0),
                active=doc.get("active", True),
                image_url=doc.get("image_url"),
                sizes=doc.get("sizes", [])
            )
        
        # Caso contrário, retornar Product
        return Product(
            id=doc["_id"],
            name=doc["name"],
            category=category,
            description=doc.get("description"),
            price=doc.get("price", 0.0),
            active=doc.get("active", True),
            image_url=doc.get("image_url")
        )

# ============== ORDER REPO ==============

class OrderRepo(Protocol):
    async def by_id(self, oid: str) -> Optional[Order]: ...
    async def save(self, o: Order) -> None: ...
    async def list_by_status(self, status: OrderStatus, skip: int = 0, limit: int = 10) -> List[Order]: ...
    async def list_all(self, skip: int = 0, limit: int = 10) -> List[Order]: ...
    async def update_status(self, oid: str, status: OrderStatus) -> None: ...

class MongoOrderRepo:
    def __init__(self, col: Any):
        self.col = col

    async def by_id(self, oid: str) -> Optional[Order]:
        """Obter pedido por ID"""
        try:
            if not oid or len(oid.strip()) == 0:
                logger.warning("ID de pedido vazio")
                return None
            
            doc = await self.col.find_one({"_id": oid})
            if not doc:
                return None
            return Order(**doc)
        except Exception as e:
            logger.error(f"Erro ao buscar pedido {oid}: {e}")
            raise ValueError(f"Erro ao buscar pedido: {str(e)}")

    async def save(self, o: Order) -> None:
        """Salvar pedido com validações"""
        try:
            # Validações
            if not o.id or len(o.id.strip()) == 0:
                raise ValueError("ID do pedido é obrigatório")
            
            if not o.items or len(o.items) == 0:
                raise ValueError("Pedido deve ter pelo menos um item")
            
            if o.total_price <= 0:
                raise ValueError("Preço total deve ser positivo")
            
            doc = o.model_dump()
            doc["_id"] = o.id
            
            result = await self.col.update_one(
                {"_id": o.id},
                {"$set": doc},
                upsert=True
            )
            
            if result.upserted_id:
                logger.info(f"Pedido criado: {o.id}")
            else:
                logger.info(f"Pedido atualizado: {o.id}")
                
        except Exception as e:
            logger.error(f"Erro ao salvar pedido {o.id}: {e}")
            raise ValueError(f"Erro ao salvar pedido: {str(e)}")

    async def list_by_status(
        self,
        status: OrderStatus,
        skip: int = 0,
        limit: int = 10
    ) -> List[Order]:
        """Listar pedidos por status com paginação"""
        try:
            if skip < 0 or limit < 1 or limit > 100:
                raise ValueError("Parâmetros de paginação inválidos")
            
            cur = self.col.find({"status": status.value}).skip(skip).limit(limit).sort("created_at", -1)
            items = []
            async for doc in cur:
                items.append(Order(**doc))
            
            logger.debug(f"Listados {len(items)} pedidos com status {status.value}")
            return items
            
        except Exception as e:
            logger.error(f"Erro ao listar pedidos por status: {e}")
            raise ValueError(f"Erro ao listar pedidos: {str(e)}")

    async def list_all(
        self,
        skip: int = 0,
        limit: int = 10
    ) -> List[Order]:
        """Listar todos os pedidos com paginação"""
        try:
            if skip < 0 or limit < 1 or limit > 100:
                raise ValueError("Parâmetros de paginação inválidos")
            
            cur = self.col.find({}).skip(skip).limit(limit).sort("created_at", -1)
            items = []
            async for doc in cur:
                items.append(Order(**doc))
            
            logger.debug(f"Listados {len(items)} pedidos")
            return items
            
        except Exception as e:
            logger.error(f"Erro ao listar pedidos: {e}")
            raise ValueError(f"Erro ao listar pedidos: {str(e)}")

    async def update_status(self, oid: str, status: OrderStatus) -> None:
        """Atualizar status do pedido"""
        try:
            if not oid or len(oid.strip()) == 0:
                raise ValueError("ID do pedido é obrigatório")
            
            result = await self.col.update_one(
                {"_id": oid},
                {"$set": {
                    "status": status.value,
                    "updated_at": datetime.utcnow()
                }}
            )
            
            if result.matched_count == 0:
                raise ValueError(f"Pedido {oid} não encontrado")
            
            logger.info(f"Status do pedido {oid} atualizado para {status.value}")
            
        except Exception as e:
            logger.error(f"Erro ao atualizar status do pedido {oid}: {e}")
            raise ValueError(f"Erro ao atualizar pedido: {str(e)}")