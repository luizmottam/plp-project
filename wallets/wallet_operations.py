from wallets.wallet import Wallet
from utils.console_operations import limpa, titulo
from utils.file_operations import save_user_wallets
import time

def print_wallets(user):
    with open(f"db/{user.user_id}.txt", 'r') as file:
        lines = file.readlines()
        if len(lines) < 4:
            print("Você ainda não tem nenhuma carteira")
        else:
            for linha in lines[4:]:
                print(linha.strip())

def create_wallet(user):
    wallet_name = input("Enter the name of the new wallet: ")
    indices = input("Enter comma-separated indices: ").split(', ')
    wallet = Wallet(wallet_name, indices)
    user.adicionar_carteira(wallet)
    print("Wallet created successfully.")
    limpa()
    print("- Wallet : ", wallet.nome)
    print("  Tickets: ", wallet.indices)
    time.sleep(2)
    limpa()
    print_wallets(user)
    save_user_wallets(user)

# NOVAS FUNÇÔES
def imprimir_carteira(user):
    with open(f"db/{user.user_id}.txt", 'r') as file:
        lines = file.readlines()
        if len(lines) < 4:
            print("Você ainda não tem nenhuma carteira")
        else:
            for linha in lines[4:]:
                print(linha.strip())
                
    return 0


def imprime_carteira(carteira):
    titulo("CARTEIRA ADICIONADA")
    print("- Carteira : ", carteira.nome)
    print("  Indices: ", carteira.indices)
    time.sleep(2)
    limpa()
     
def criar_carteira(user):
    titulo("Nova Carteira")
    nome_da_carteira = input("Nome da Cartiera: ")
    indices = input("Indices (digite separado por ,): ")
    carteira = Wallet(nome_da_carteira, indices)
    
    esc = input("Deseja adicionar carteira a suas carteiras (s/n)? ").upper()
    if esc == 'S':
        user.adicionar_carteira(carteira)
        imprime_carteira(carteira)
    print(f"A carteira {nome_da_carteira} foi descartada")