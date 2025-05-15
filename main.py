# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# Permite acesso do frontend (pode colocar seu domínio do frontend em allowed_origins)
origins = [
    
    "https://chatbot-frontend-ijd5.onrender.com",  # exemplo do render static site
    "*",  # permite qualquer origem (para teste, não recomendado em produção)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Mensagem(BaseModel):
    mensagem: str

@app.get("/")
def home():
    return {"message": "Olá, mundo! Esta é minha primeira API no Render."}

@app.post("/chat")

def chat(mensagem: Mensagem):
    texto = mensagem.mensagem
    resposta = f"Mensagem recebida: {texto} (conexão OK!)"
    return {"resposta": resposta}
