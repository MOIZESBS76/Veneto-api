from __future__ import annotations
import os
from pathlib import Path
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(dotenv_path=ROOT / ".env")

MONGO_URL: str = os.getenv("MONGO_URL", "")
MONGO_DB: str = os.getenv("MONGO_DB", "chatdb")
APP_HOST: str = os.getenv("APP_HOST", "0.0.0.0")
APP_PORT: int = int(os.getenv("APP_PORT", "8000"))

if not MONGO_URL:
	# Não bloquear a importação — levantamos erro apenas quando tentamos conectar ao DB
	pass
