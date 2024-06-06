import time
from funcoes.limpa import limpa
from servicos.ContaService import ContaService
from utils.Utils import criar_carteira, print_carteiras

class AuthService:
    @staticmethod
    def autentificacao_de_senha(usuario):
        user_id = None
        # Find the user ID
        with open(f"users/user_info.txt", "r") as file:
            for line in file:
                if line.startswith(f"User [{usuario.nome}] ID: "):
                    user_id = line.split(":")[1].strip()
                    usuario.user_id = user_id
                    break
        # Check the password
        if user_id:
            with open(f"users/{user_id}.txt", "r") as file:
                for line in file:
                    if line.startswith("Passwd: "):
                        senha = line.split(":")[1].strip()
                        if usuario.senha == senha:
                            return 1
        print("Senha incorreta!")
        return 0

    @staticmethod
    def autentificacao_de_usuario(usuario):
        with open("users/user_info.txt", "r") as file:
            for line in file:
                if line.startswith(f"User [{usuario.nome}] ID: "):
                    return 1
        return 0

    @staticmethod
    def authenticator(esc, usuario):
        # SIGN UP
        if esc == 1:
            if AuthService.autentificacao_de_usuario(usuario) == 1:
                print("Usuário já existe")
            else:
                ContaService.criar_usuario(usuario)
                print(f"Welcome {usuario.nome}")
                time.sleep(5)
                limpa()
                esc1 = int(input("2. Criar carteira? "))
                if esc1 == 2:
                    criar_carteira(usuario)
                else:
                    print_carteiras(usuario)

        elif esc == 2:
            if AuthService.autentificacao_de_usuario(usuario) == 1 and AuthService.autentificacao_de_senha(usuario) == 1:
                print(f"Welcome {usuario.nome}")
                time.sleep(5)
                limpa()
                esc1 = int(input("2. Criar carteira? "))
                if esc1 == 2:
                    criar_carteira(usuario)
                else:
                    print_carteiras(usuario)

            elif AuthService.autentificacao_de_usuario(usuario) == 0:
                print("Usuário não existe!")
            else:
                print("Alguma coisa errada aconteceu!\n")

        return usuario
