import time

from Scripts.Class.Usuario import Usuario
from Scripts.Class.Carteira import Carteira
from utils.Utils import limpa


def print_carteiras(usuario):
    linha_inicial = 4
    with open(f"Users/{usuario.user_id}.txt", 'r') as file:
        lines = file.readlines()  # Lê todas as linhas do arquivo em uma lista

        # Verifica se a linha inicial está dentro dos limites do arquivo
        if linha_inicial < 1 or linha_inicial > len(lines):
            print("Você ainda não tem nenhuma carteira")
        else:
            # Imprime as linhas a partir da linha inicial
            for linha in lines[linha_inicial - 1:]:
                print(linha.strip())


def criar_carteira(usuario):
    nome_carteira = input("Enter the name of the new wallet: ")
    tickets = input("Enter comma-separated indices: ").split(', ')
    carteira = Carteira(nome_carteira, tickets)
    print(usuario.adicionarticket(carteira))
    print("Wallet created successfully.")
    limpa()
    print("- Wallet : ", carteira.nome)
    print("  Tickets: ", carteira.tickets)
    time.sleep(2)
    limpa()
    usuario.print_carteiras(usuario)

    with open(f"Users/{usuario.user_id}.txt", "a") as file:
        for wallet in usuario.carteiras:
            file.write(f"- Wallet Name: {carteira.nome}\n")
            file.write(f"  Tickets: {', '.join(carteira.tickets)}\n")
        file.write("\n")


class CarteiraService:
    @staticmethod
    def criar_carteira_para_usuario(usuario: Usuario, nome_carteira: str) -> Carteira:
        nova_carteira = Carteira(nome_carteira)
        usuario.adicionar_carteira(nova_carteira)
        return nova_carteira

    @staticmethod
    def adicionar_ticket_na_carteira(carteira: Carteira, ticket: str):
        carteira.adicionarticket(ticket)
