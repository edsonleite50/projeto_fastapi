import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from pessoa import Pessoa
from pessoa_operations import PessoaOperations

app = FastAPI()

class PessoaInput(BaseModel):
    codigo: int
    nome: str

@app.get("/exemplo")
def example() -> str:
    return "Olá mundo"

@app.post("/exemplo_2")
def example2(pessoa: PessoaInput) -> str:
    return str(pessoa.codigo)

@app.get("/pegar_pessoa_por_nome")
async def get_nome_pessoa(nome: str) -> dict:
    return await PessoaOperations.get_nome_pessoa(nome)

@app.post("/inserir_pessoa")
async def inserir_pessoa(pessoa: PessoaInput) -> str:
    return await PessoaOperations.inserir_pessoa(pessoa)

if __name__ == "__main__": 
    print(example())
    uvicorn.run("api:app", port=8087, workers=2, reload=True)
    