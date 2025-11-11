import pytest
from unittest.mock import AsyncMock, MagicMock
from app.infra.repos import MongoProductRepo, MongoOrderRepo
from app.domain.entities import Product, ProductCategory
from app.services.product_service import ProductService
from app.services.order_service import OrderService

@pytest.fixture
async def mock_product_repo():
    """Mock do repositório de produtos"""
    repo = AsyncMock(spec=MongoProductRepo)
    repo.by_id = AsyncMock(return_value=None)
    repo.save = AsyncMock()
    repo.list_active = AsyncMock(return_value=[])
    repo.list_by_category = AsyncMock(return_value=[])
    return repo

@pytest.fixture
async def mock_order_repo():
    """Mock do repositório de pedidos"""
    repo = AsyncMock(spec=MongoOrderRepo)
    repo.by_id = AsyncMock(return_value=None)
    repo.save = AsyncMock()
    repo.list_all = AsyncMock(return_value=[])
    repo.list_by_status = AsyncMock(return_value=[])
    repo.update_status = AsyncMock()
    return repo

@pytest.fixture
async def product_service(mock_product_repo):
    """Serviço de produtos com mock"""
    return ProductService(mock_product_repo)

@pytest.fixture
async def order_service(mock_order_repo):
    """Serviço de pedidos com mock"""
    return OrderService(mock_order_repo)