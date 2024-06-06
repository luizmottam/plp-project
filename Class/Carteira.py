from typing import List


class Carteira:
    def __init__(self, nome: str, tickets: List):
        self.nome = nome
        self.tickets: List[str] = []

    def adicionarticket(self, ticket: str):
        self.tickets.append(ticket)

    def __repr__(self):
        return f"Carteira(nome={self.nome}, tickets={self.tickets})"
