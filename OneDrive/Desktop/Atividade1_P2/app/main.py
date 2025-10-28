# FastAPI: endpoint /enviar
from .producer_rabbit import send_message
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Mensagem(BaseModel):
    nome: str
    texto: str

@app.post("/enviar")
def enviar(mensagem: Mensagem):
    send_message(mensagem.dict())
    return {"status": "Mensagem enviada com sucesso!"}
