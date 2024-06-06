import time

from test import create_account
from utils.Utils import limpa
from servicos.CarteriaService import criar_carteira, print_carteiras





    def passwd_authentication(usuario):
        user_id = None
        # Find the user ID
        with open(f"Usuarios/user_info.txt", "r") as file:
            for line in file:
                if line.startswith(f"User [{usuario.nome}] ID: "):
                    user_id = line.split(":")[1].strip()
                    usuario.user_id = user_id
                    break
        # Check the password
        with open(f"Users/{user_id}.txt", "r") as file:
            for line in file:
                if line.startswith("Passwd: "):
                    senha = line.split(":")[1].strip()
                    if usuario.senha == senha:
                        return 1
        print("Senha incorreta!")
        return 0


    def user_authentication(usuario):
        with open("Usuarios/user_info.txt", "r") as file:
            for line in file:
                if line.startswith(f"User [{usuario.nome}] ID: "):
                    return 1
        return 0


    def authenticator(esc, usuario):
        # SIGN UP
        if esc == 1:
            if user_authentication(usuario) == 1:
                print("Usuário já existe")
            else:
                create_account(usuario)
                print(f"Welcome {usuario.nome}")
                time.sleep(5)
                limpa()
                esc1 = int(input("2. Criar carteira? "))
                if esc1 == 2:
                    criar_carteira(usuario)
                else:
                    print_carteiras(usuario)


        elif esc == 2:
            if user_authentication(usuario) == 1 and passwd_authentication(usuario) == 1:
                print(f"Welcome {usuario.nome}")
                time.sleep(5)
                limpa()
                esc1 = int(input("2. Criar carteira? "))
                if esc1 == 2:
                    criar_carteira(usuario)
                else:
                    print_carteiras(usuario)


            elif user_authentication(usuario) == 0:
                print("Usuário não existe!")
            else:
                print("Alguma coisa errada aconteceu!\n")

        return usuario
