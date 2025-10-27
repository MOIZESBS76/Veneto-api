from fastapi import FastAPI
from app.core.settings import settings
from app.core.logging import setup_logging
from app.api.routers import health, products

setup_logging()
app = FastAPI(title=settings.APP_NAME)

app.include_router(health.router)
app.include_router(products.router)

from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Veneto API online"}

# Atualização dos router de orders
from fastapi import FastAPI
from app.core.settings import settings
from app.core.logging import setup_logging
from app.api.routers import health, products, orders

setup_logging()
app = FastAPI(title=settings.APP_NAME)

app.include_router(health.router)
app.include_router(products.router)
app.include_router(orders.router)

@app.get("/")
async def root():
    return {"message": "Veneto API online"}
