import time
from funcoes.limpa import limpa

class ContaService:
    @staticmethod
    def criar_usuario(usuario):
        # Add info public
        with open("users/user_info.txt", "a") as file:
            file.write(f"User [{usuario.nome}] ID: {usuario.user_id}\n")

        # Add info private
        with open(f"users/{usuario.user_id}.txt", "w") as file:
            file.write(f"Essa carteira pertence a {usuario.nome}\n")
            file.write(f"Passwd: {usuario.senha}\n")
            file.write(f"Wallets: {usuario.carteiras}\n")

        print("Usuário criado\n")
        time.sleep(5)
        limpa()
