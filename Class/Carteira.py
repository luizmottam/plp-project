class Carteira:
    def __init__(self, nome: str, tickets=None):
        if tickets is None:
            tickets = []
        self.nome = nome
        self.tickets = tickets

    def adicionarticket(self, ticket: str):
        self.tickets.append(ticket)

    def __repr__(self):
        return f"Carteira(nome={self.nome}, tickets={self.tickets})"
