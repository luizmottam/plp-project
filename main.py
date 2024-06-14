import getpass
import time
from utils.console_operations import limpa, titulo
from users.user_operations import criacao_do_usuario, conta_do_usuario, autentifica_senha
from wallets.wallet_operations import imprimir_carteira, criar_carteira, deletar_carteira_do_usuario

def menu_login():
    while True:
        try:
            limpa()
            print("1. Cadastrar-se\n2. Entrar com usuário")
            esc = int(input("Escolha: "))
            if esc in [1, 2]:
                return esc
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def menu_de_operacoes_carteira():
    while True:
        try:
            print("1. Ver carteira(s)\n2. Adicionar carteira\n3. Deletar carteira(s)\n4. Sair")
            esc = int(input("Escolha: "))
            if esc in range(1, 5):
                return esc
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
                 
def main():
    while True:
        escolha_login = menu_login()
        if escolha_login == 1:
            criacao_do_usuario()
            time.sleep(3)
            limpa()
        elif escolha_login == 2:
            user = conta_do_usuario()
            time.sleep(3)
            limpa()
            if user and autentifica_senha(user):
                while True:
                    escolha_carteira = menu_de_operacoes_carteira()
                    if escolha_carteira == 1:
                        imprimir_carteira(user)
                        time.sleep(3)
                        limpa()
                    elif escolha_carteira == 2:
                        criar_carteira(user)
                        time.sleep(3)
                        limpa()
                    elif escolha_carteira == 3:
                        deletar_carteira_do_usuario(user)
                        time.sleep(3)
                        limpa()
                    elif escolha_carteira == 4:
                        print("Saindo do menu de carteiras.")
                        time.sleep(3)
                        break

                
if __name__ == "__main__":
    main()
