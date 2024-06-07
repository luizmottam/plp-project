import uuid

class User:
    def __init__(self, email, nome, senha) -> None:
        self.id_usuario = str(uuid.uuid4())
        self.email = email
        self.nome = nome
        self.senha = senha
        self.carteiras = []

    def adiconar_carteira(self, carteira):
        self.carteiras.append(carteira)
