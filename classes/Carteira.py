from typing import List

class Carteira:
    def __init__(self, nome: str):
        self.nome = nome
        self.tickets: List[str] = []

    def adicionarTicket(self, ticket: str):
        self.tickets.append(ticket)
    
    def __repr__(self):
        return f"Carteira(nome={self.nome}, tickets={self.tickets})"
