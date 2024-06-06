import getpass
import os

from Scripts.Class.Usuario import Usuario


def limpa():
    os.system("cls")


class Utils:

    @staticmethod
    def conta_usuario():
        nome = str(input("Entre com nome de usuário: "))
        senha = getpass.getpass("Sua senha: ")
        usuario = Usuario(nome, senha)  # insere as informações a um usuário
        return usuario
