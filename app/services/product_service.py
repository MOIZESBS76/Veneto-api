from app.domain.entities import Product
from app.infra.repos import ProductRepo

class ProductService:
    def __init__(self, repo: ProductRepo):
        self.repo = repo

    async def create(self, p: Product) -> Product:
        exists = await self.repo.by_id(p.id)
        if exists:
            raise ValueError("Produto já existe")
        # Regras de negócio futuras (promoções, validações etc.)
        await self.repo.save(p)
        return p

    async def list_active(self) -> list[Product]:
        return await self.repo.list_active()