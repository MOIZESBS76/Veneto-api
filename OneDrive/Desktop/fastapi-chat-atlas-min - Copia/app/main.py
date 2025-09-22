from __future__ import annotations
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from .config import APP_HOST, APP_PORT
from .database import get_db, serialize
from .ws_manager import WSManager
from .routers import messages

app = FastAPI(title="FastAPI Chat + MongoDB Atlas (refatorado)")

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# WebSocket manager
manager = WSManager()

# Routers REST
app.include_router(messages.router)

# --- Static files ---
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Caminho para index.html
INDEX_FILE = "app/static/html/index.html"

@app.get("/", include_in_schema=False)
async def index():
    """
    Serve a página principal do chat.
    """
    return FileResponse(INDEX_FILE)

# --- WebSocket endpoint ---
@app.websocket("/ws/{room}")
async def ws_room(ws: WebSocket, room: str):
    """
    WebSocket para sala de chat.
    Envia histórico inicial e recebe mensagens novas.
    """
    await manager.connect(room, ws)
    try:
        # histórico inicial
        cursor = get_db()["messages"].find({"room": room}).sort("_id", -1).limit(20)
        items = [serialize(d) async for d in cursor]
        items.reverse()
        await ws.send_json({"type": "history", "items": items})

        # loop de mensagens
        while True:
            payload = await ws.receive_json()
            username = str(payload.get("username", "anon"))[:50]
            content = str(payload.get("content", "")).strip()
            if not content:
                continue  # não persistir mensagens vazias
            doc = {
                "room": room,
                "username": username,
                "content": content,
                "created_at": __import__("datetime").datetime.now(__import__("datetime").timezone.utc),
            }
            res = await get_db()["messages"].insert_one(doc)
            doc["_id"] = res.inserted_id
            await manager.broadcast(room, {"type": "message", "item": serialize(doc)})

    except WebSocketDisconnect:
        manager.disconnect(room, ws)
    except Exception as exc:
        # fecha a conexão em caso de erro inesperado
        try:
            await ws.close()
        except Exception:
            pass
        raise HTTPException(status_code=500, detail=str(exc))
