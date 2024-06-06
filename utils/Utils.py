import getpass
import time
from Class.Usuario import Usuario
from Class.Carteira import Carteira
from funcoes.limpa import limpa

class Utils:
    @staticmethod
    def conta_usuario():
        nome = str(input("Entre com nome de usuário: "))
        senha = getpass.getpass("Sua senha: ")
        email = str(input("Seu email: "))
        usuario = Usuario(nome, senha, email)  # insere as informações a um usuário
        return usuario

def print_carteiras(usuario):
    linha_inicial = 4
    with open(f"users/{usuario.user_id}.txt", 'r') as file:
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
    usuario.adicionar_carteira(carteira)
    print("Wallet created successfully.")
    limpa()
    print("- Wallet : ", carteira.nome)
    print("  Tickets: ", carteira.tickets)
    time.sleep(2)
    limpa()
    print_carteiras(usuario)

    with open(f"users/{usuario.user_id}.txt", "a") as file:
        for wallet in usuario.carteiras:
            file.write(f"- Wallet Name: {carteira.nome}\n")
            file.write(f"  Tickets: {', '.join(carteira.tickets)}\n")
        file.write("\n")
