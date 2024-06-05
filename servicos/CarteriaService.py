from classes.Usuario import Usuario
from classes.Carteira import Carteira

class CarteiraService:
    @staticmethod
    def criarCarteiraParaUsuario(usuario: Usuario, nome_carteira: str) -> Carteira:
        nova_carteira = Carteira(nome=nome_carteira)
        usuario.adicionarCarteira(nova_carteira)
        return nova_carteira

    @staticmethod
    def adicionaTicketNaCarteira(carteira: Carteira, ticket: str):
        carteira.adicionarTicket(ticket)