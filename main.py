# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Mensagem(BaseModel):
    mensagem: str

@app.get("/")
def home():
    return {"message": "Olá, mundo! Esta é minha primeira API no Render."}

@app.post("/chat")
def chat(mensagem: Mensagem):
    texto = mensagem.mensagem
    resposta = f"Você disse: {texto}"
    return {"resposta": resposta}