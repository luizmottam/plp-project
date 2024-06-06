import getpass
import os

from Class.Usuario import Usuario


class Utils:

    @staticmethod
    def limpa():
        os.system("cls")

    @staticmethod
    def conta_usuario():
        nome = str(input("Entre com nome de usuário: "))
        senha = getpass.getpass("Sua senha: ")
        usuario = Usuario(nome, senha)  # insere as informações a um usuário
        return usuario
