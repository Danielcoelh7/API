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
    resposta =  "Resposta da IA:\n"
            "O conceito de conjunto numérico é abordado em duas disciplinas do contexto fornecido, dependendo do nível de ensino:\n\n"
            "1. No Curso Técnico em Informática Integrado ao Ensino Médio, em Matemática 1 (1º ano, 1º semestre, CBTMMA1):\n"
            "- Conjuntos numéricos: propriedades, operações e representações.\n"
            "- Conjuntos: notação; operações; resolução de problemas.\n"
            "- Intervalos reais: representação; operações (união, diferença e intersecção).\n\n"
            "2. No Curso Superior de Tecnologia em Automação Industrial, em Cálculo Diferencial e Integral 1 (1º semestre, CBTCDI1):\n"
            "- Conjuntos numéricos: Operações entre conjuntos.\n"
            "- Conjunto dos números naturais, inteiros, racionais e reais. Intervalos reais.\n"
            "- Notação para representar conjuntos."
    return {"resposta": resposta}
