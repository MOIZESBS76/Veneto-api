from __future__ import annotations
from fastapi import APIRouter, Query, HTTPException, status, Body
from bson import ObjectId
from typing import Optional

from ..database import get_db, serialize
from ..models import MessageIn, MessageOut, MessagesPage

router = APIRouter()

@router.get("/rooms/{room}/messages", response_model=MessagesPage)
async def get_messages(
	room: str, limit: int = Query(20, ge=1, le=100), before_id: Optional[str] = Query(None)
):
	# Retorna mensagens paginadas de uma sala.
	# Se before_id for inválido, retorna 400 (Bad Request).
	query = {"room": room}
	if before_id:
		try:
			query["_id"] = {"$lt": ObjectId(before_id)}
		except Exception:
			raise HTTPException(
				status_code=status.HTTP_400_BAD_REQUEST, detail="before_id inválido"
			)

	cursor = get_db()["messages"].find(query).sort("_id", -1).limit(limit)
	docs = [serialize(d) async for d in cursor]
	docs.reverse()
	next_cursor = docs[0]["_id"] if docs else None
	# map to MessageOut
	items = [MessageOut(**d) for d in docs]
	return {"items": items, "next_cursor": next_cursor}

@router.post("/rooms/{room}/messages", status_code=201, response_model=MessageOut)
async def post_message(room: str, payload: MessageIn = Body(...)):
	# Cria uma nova mensagem.
	# Valida conteúdo através de Pydantic; não salva mensagens vazias.

	doc = {
		"room": room,
		"username": payload.username,
		"content": payload.content,
		"created_at": __import__("datetime").datetime.now(__import__("datetime").timezone.utc),
	}
	res = await get_db()["messages"].insert_one(doc)
	doc["_id"] = res.inserted_id
	return MessageOut(**serialize(doc))
