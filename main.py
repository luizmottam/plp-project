import getpass
import time
from utils.console_operations import limpa, titulo
from users.user_operations import criacao_do_usuario, conta_do_usuario, autentifica_senha
from wallets.wallet_operations import imprimir_carteira, criar_carteira

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
            print("1. Ver carteira(s)\n2. Adicionar carteira\n3. Editar carteira(s)\n4. Deletar carteira(s)\n5. Sair")
            esc = int(input("Escolha: "))
            if esc in range(1, 6):
                return esc
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def menu_de_operacoes_ticket():
    while True:
        try:
            print("1. Ver ticket(s)\n2. Adicionar ticket\n3. Editar ticket(s)\n4. Deletar ticket(s)\n5. Sair")
            esc = int(input("Escolha: "))
            if esc in range(1, 6):
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
        elif escolha_login == 2:
            user = conta_do_usuario()
            if user and autentifica_senha(user):
                while True:
                    escolha_carteira = menu_de_operacoes_carteira()
                    if escolha_carteira == 1:
                        imprimir_carteira(user)
                    elif escolha_carteira == 2:
                        criar_carteira(user)
                    elif escolha_carteira == 3:
                        print("Editar carteira(s) selecionado.")
                        # Adicione o código para editar carteiras aqui
                        while True:
                            escolha_ticket = menu_de_operacoes_ticket()
                            if escolha_ticket == 1:
                                print("Ver ticket(s) selecionado.")
                                # Adicione o código para ver tickets aqui
                            elif escolha_ticket == 2:
                                print("Adicionar ticket selecionado.")
                                # Adicione o código para adicionar ticket aqui
                            elif escolha_ticket == 3:
                                print("Editar ticket(s) selecionado.")
                                # Adicione o código para editar tickets aqui
                            elif escolha_ticket == 4:
                                print("Deletar ticket(s) selecionado.")
                                # Adicione o código para deletar tickets aqui
                            elif escolha_ticket == 5:
                                print("Saindo do menu de tickets.")
                                break
                    elif escolha_carteira == 4:
                        print("Deletar carteira(s) selecionado.")
                        # Adicione o código para deletar carteiras aqui
                    elif escolha_carteira == 5:
                        print("Saindo do menu de carteiras.")
                        break

                

if __name__ == "__main__":
    main()
