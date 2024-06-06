import uuid
from typing import List
from Class.Carteira import Carteira

class Usuario:
    def __init__(self, nome: str, senha: str, email: str):
        self.user_id = str(uuid.uuid4())
        self.nome = nome
        self.senha = senha
        self.email = email
        self.carteiras: List[Carteira] = []

    def adicionar_carteira(self, carteira: Carteira):
        self.carteiras.append(carteira)

    def __repr__(self):
        return f"Usuario(nome={self.nome}, id={self.user_id}, email={self.email}, senha={self.senha}, carteiras={self.carteiras})"
