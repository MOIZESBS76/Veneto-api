FROM python:3.11-slim

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY pyproject.toml /app/pyproject.toml
RUN pip install --no-cache-dir uvicorn fastapi motor pydantic[dotenv] httpx pytest pytest-asyncio

COPY app /app/app
CMD ["uvicorn", "app.main:app", "--host","0.0.0.0", "--port","8000"]