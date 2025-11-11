import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app
from app.domain.entities import Product, Pizza, PizzaSize, ProductCategory

# Testes de validação (sem precisar de mock)

@pytest.mark.asyncio
async def test_create_product_invalid_price():
    """Testar validação de preço negativo"""
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as ac:
        payload = {
            "id": "bebida_002",
            "name": "Refrigerante",
            "category": "bebida",
            "price": -5.50
        }
        r = await ac.post("/products", json=payload)
        assert r.status_code == 422

@pytest.mark.asyncio
async def test_create_product_invalid_image_url():
    """Testar validação de URL de imagem"""
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as ac:
        payload = {
            "id": "bebida_003",
            "name": "Refrigerante",
            "category": "bebida",
            "price": 5.50,
            "image_url": "invalid-url"
        }
        r = await ac.post("/products", json=payload)
        assert r.status_code == 422

@pytest.mark.asyncio
async def test_create_pizza_without_sizes():
    """Testar que pizza sem tamanhos falha"""
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as ac:
        payload = {
            "id": "pizza_002",
            "name": "Pizza Vazia",
            "price": 25.00,
            "sizes": []
        }
        r = await ac.post("/products/pizzas", json=payload)
        assert r.status_code == 422

@pytest.mark.asyncio
async def test_create_pizza_invalid_size():
    """Testar validação de tamanho de pizza (muito pequeno)"""
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as ac:
        payload = {
            "id": "pizza_003",
            "name": "Pizza Inválida",
            "price": 25.00,
            "sizes": [
                {"size_cm": 10, "price": 25.00}
            ]
        }
        r = await ac.post("/products/pizzas", json=payload)
        assert r.status_code == 422

@pytest.mark.asyncio
async def test_create_pizza_invalid_size_too_large():
    """Testar validação de tamanho de pizza (muito grande)"""
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as ac:
        payload = {
            "id": "pizza_006",
            "name": "Pizza Gigante",
            "price": 25.00,
            "sizes": [
                {"size_cm": 150, "price": 25.00}
            ]
        }
        r = await ac.post("/products/pizzas", json=payload)
        assert r.status_code == 422

@pytest.mark.asyncio
async def test_create_product_missing_required_field():
    """Testar que faltam campos obrigatórios"""
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as ac:
        payload = {
            "id": "bebida_005",
            "name": "Refrigerante"
            # falta category e price
        }
        r = await ac.post("/products", json=payload)
        assert r.status_code == 422

@pytest.mark.asyncio
async def test_pizza_valid_sizes():
    """Testar que validação passa com tamanhos válidos"""
    # Apenas verificar que o modelo aceita os tamanhos
    sizes = [
        PizzaSize(size_cm=30, price=20.00),
        PizzaSize(size_cm=40, price=30.00),
        PizzaSize(size_cm=50, price=40.00)
    ]
    
    pizza = Pizza(
        id="pizza_test",
        name="Test Pizza",
        category=ProductCategory.PIZZA,
        price=20.00,
        sizes=sizes
    )
    
    assert pizza.id == "pizza_test"
    assert len(pizza.sizes) == 3
    assert pizza.sizes[0].size_cm == 30

@pytest.mark.asyncio
async def test_product_valid_with_image():
    """Testar que produto válido com imagem é aceito"""
    product = Product(
        id="test_001",
        name="Test Product",
        category=ProductCategory.BEBIDA,
        price=10.00,
        image_url="https://example.com/image.jpg"
    )
    
    assert product.id == "test_001"
    assert product.price == 10.00
    assert product.active is True

@pytest.mark.asyncio
async def test_product_price_rounding():
    """Testar que preço é arredondado para 2 casas decimais"""
    product = Product(
        id="test_002",
        name="Test",
        category=ProductCategory.BEBIDA,
        price=10.999
    )
    
    assert product.price == 11.00  # Arredondado

@pytest.mark.asyncio
async def test_pizza_price_validation():
    """Testar validação de preço zero em pizza"""
    with pytest.raises(ValueError):
        PizzaSize(size_cm=35, price=0)

@pytest.mark.asyncio
async def test_pizza_negative_price_validation():
    """Testar validação de preço negativo em pizza"""
    with pytest.raises(ValueError):
        PizzaSize(size_cm=35, price=-10.00)