from __future__ import annotations
from typing import Optional
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from datetime import datetime, timezone

from .config import MONGO_URL, MONGO_DB

_client: Optional[AsyncIOMotorClient] = None

def get_db():
	# Retorna a instância do banco (coleção/DB).
	# Inicializa o cliente na primeira chamada.
	# Lança RuntimeError se MONGO_URL não estiver configurada.
	global _client
	if _client is None:
		if not MONGO_URL:
			raise RuntimeError("Defina MONGO_URL no .env (string do MongoDB Atlas).")
		_client = AsyncIOMotorClient(MONGO_URL)
	return _client[MONGO_DB]

def iso(dt: datetime) -> str:
	if dt.tzinfo is None:
		dt = dt.replace(tzinfo=timezone.utc)
	return dt.isoformat()

def serialize(doc: dict) -> dict:
	# Serializa documentos do Mongo para JSON-friendly dict.
	# Converte ObjectId para string e created_at para ISO.
	d = dict(doc)
	if "_id" in d:
		d["_id"] = str(d["_id"])
	if "created_at" in d and isinstance(d["created_at"], datetime):
		d["created_at"] = iso(d["created_at"])
	return d
