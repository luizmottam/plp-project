import os

def limpa():
    os.system("cls" if os.name == "nt" else "clear")

def titulo(texto):
    print("{:=^30}".format(texto))

