from Class.Usuario import Usuario
from Class.Carteira import Carteira

class CarteiraService:
    @staticmethod
    def criar_carteira_para_usuario(usuario: Usuario, nome_carteira: str) -> Carteira:
        nova_carteira = Carteira(nome_carteira)
        usuario.adicionar_carteira(nova_carteira)
        return nova_carteira

    @staticmethod
    def adicionar_ticket_na_carteira(carteira: Carteira, ticket: str):
        carteira.adicionarticket(ticket)
