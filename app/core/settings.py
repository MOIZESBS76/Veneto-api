# app/core/settings.py (compatível com Pydantic v2)
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "Veneto API"
    MONGO_URI: str = "mongodb://localhost:27017"
    MONGO_DB: str = "veneto"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()