from pydantic import BaseModel

class Pessoa(BaseModel):
    "Classe modelo de objetos do tipo Pessoa"
    
    
    def __init__(self, nome: str, email: str, mensagem: str) -> None:
        self.nome = nome
        self.email = email
        self.mensagem = mensagem
        
  