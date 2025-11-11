from app.domain.entities import Product, ProductCategory
from app.infra.repos import ProductRepo

class ProductService:
    def __init__(self, repo: ProductRepo):
        self.repo = repo

    async def create(self, p: Product) -> Product:
        """Criar um novo produto com validações"""
        exists = await self.repo.by_id(p.id)
        if exists:
            raise ValueError("Produto já existe")
        
        # Validações de negócio
        if p.price <= 0:
            raise ValueError("Preço deve ser positivo")
        
        if p.category == "pizza" and hasattr(p, 'sizes'):
            if not p.sizes or len(p.sizes) == 0:
                raise ValueError("Pizza deve ter pelo menos um tamanho")
        
        await self.repo.save(p)
        return p

    async def list_active(self, skip: int = 0, limit: int = 10) -> list[Product]:
        """Listar todos os produtos ativos com paginação"""
        if skip < 0 or limit < 1 or limit > 100:
            raise ValueError("Parâmetros de paginação inválidos")
        return await self.repo.list_active(skip=skip, limit=limit)

    async def list_by_category(
        self,
        category: ProductCategory,
        skip: int = 0,
        limit: int = 10
    ) -> list[Product]:
        """Listar produtos por categoria com paginação"""
        if skip < 0 or limit < 1 or limit > 100:
            raise ValueError("Parâmetros de paginação inválidos")
        return await self.repo.list_by_category(category, skip=skip, limit=limit)

    async def get_by_id(self, product_id: str) -> Product:
        """Obter um produto pelo ID"""
        if not product_id or len(product_id) == 0:
            raise ValueError("ID do produto inválido")
        product = await self.repo.by_id(product_id)
        if not product:
            raise ValueError(f"Produto {product_id} não encontrado")
        return product

    async def update(self, product_id: str, data: dict) -> Product:
        """Atualizar um produto"""
        product = await self.get_by_id(product_id)
        
        # Validar preço se estiver sendo atualizado
        if 'price' in data and data['price'] <= 0:
            raise ValueError("Preço deve ser positivo")
        
        # Atualizar campos
        for key, value in data.items():
            if hasattr(product, key):
                setattr(product, key, value)
        
        await self.repo.save(product)
        return product

    async def deactivate(self, product_id: str) -> Product:
        """Desativar um produto (soft delete)"""
        product = await self.get_by_id(product_id)
        product.active = False
        await self.repo.save(product)
        return product