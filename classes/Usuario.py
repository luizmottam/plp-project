from typing import List
from Carteira import Carteira

class Usuario:
    def __init__(self, nome: str, email: str):
        self.nome = nome
        self.email = email
        self.carteiras: List[Carteira] = []

    def adicionarCarteira(self, carteira: Carteira):
        self.carteiras.append(carteira)
    
    def __repr__(self):
        return f"Usuario(nome={self.nome}, email={self.email}, carteiras={self.carteiras})"
