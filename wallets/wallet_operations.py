from wallets.wallet import Wallet
from utils.console_operations import limpa
import time

def print_wallets(user):
    with open(f"Users/{user.user_id}.txt", 'r') as file:
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
    user.add_wallet(wallet)
    print("Wallet created successfully.")
    limpa()
    print("- Wallet : ", wallet.nome)
    print("  Tickets: ", wallet.indices)
    time.sleep(2)
    limpa()
    print_wallets(user)
    save_user_wallets(user)
