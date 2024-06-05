import getpass
import uuid
import time
import os


# CLASSES PRINCIPAIS
class Wallet:

  def __init__(self, name, tickets) -> None:
    self.nome = name
    self.indices = tickets


class User:

  def __init__(self, nickname, passwd) -> None:
    self.user_id = str(uuid.uuid4())
    self.nickname = nickname
    self.passwd = passwd
    self.wallets = []

  def add_wallet(self, wallet):
    self.wallets.append(wallet)


# FUNÇÕES
def limpa():
  os.system("clear")


def user_account():
  nickname = str(input("Entre com nome de usuário: "))
  password = getpass.getpass("Sua senha: ")
  user = User(nickname, password)  #insere as informações a um usuário
  return user


# Wallets

def print_wallets(user):
  linha_inicial = 4
  with open(f"Users/{user.user_id}.txt", 'r') as file:
    lines = file.readlines()  # Lê todas as linhas do arquivo em uma lista

    # Verifica se a linha inicial está dentro dos limites do arquivo
    if linha_inicial < 1 or linha_inicial > len(lines):
      print("Você ainda não tem nenhuma carteira")
    else:
      # Imprime as linhas a partir da linha inicial
      for linha in lines[linha_inicial - 1:]:
        print(linha.strip())

# Function to save user information to the text file
def create_wallet(user):
  wallet_name = input("Enter the name of the new wallet: ")
  indices = input("Enter comma-separated indices: ").split(', ')
  wallet = Wallet(wallet_name, indices)
  print(user.add_wallet(wallet))
  print("Wallet created successfully.")
  limpa()
  print("- Wallet : ", wallet.nome)
  print("  Tickets: ", wallet.indices)
  time.sleep(2)
  limpa()
  print_wallets(user)
  
  with open(f"Users/{user.user_id}.txt", "a") as file:
    for wallet in user.wallets:
      file.write(f"- Wallet Name: {wallet.nome}\n")
      file.write(f"  Tickets: {', '.join(wallet.indices)}\n")
    file.write("\n")


# INSERE OS REGISTROS DE UMA NOVA CONTA
def create_account(user):
  # Add info public
  with open("Users/user_info.txt", "a") as file:
    file.write(f"User [{user.nickname}] ID: {user.user_id}\n")

  # Add info private
  with open(f"Users/{user.user_id}.txt", "w") as file:
    file.write(f"Essa carteira pertence a {user.nickname}\n")
    file.write(f"Passwd: {user.passwd}\n")
    file.write(f"Wallets: {user.wallets}\n")

  print("Usuário criado\n")
  time.sleep(5)
  limpa()


#FUNÇÕES - VERIFICAÇÕES


# Verifica se a senha está correta
def passwd_authentication(user):
  user_id = None
  # Find the user ID
  with open(f"Users/user_info.txt", "r") as file:
    for line in file:
      if line.startswith(f"User [{user.nickname}] ID: "):
        user_id = line.split(":")[1].strip()
        user.user_id = user_id
        break
  # Check the password
  with open(f"Users/{user_id}.txt", "r") as file:
    for line in file:
      if line.startswith("Passwd: "):
        passwd = line.split(":")[1].strip()
        if user.passwd == passwd:
          return 1
  print("Senha incorreta!")
  return 0


# Verifica se o usuário já existe
def user_authentication(user):
  with open("Users/user_info.txt", "r") as file:
    for line in file:
      if line.startswith(f"User [{user.nickname}] ID: "):
        return 1
  return 0


def authenticator(esc, user):
  # SIGN UP
  if esc == 1:
    if user_authentication(user) == 1:
      print("Usuário já existe")
    else:
      create_account(user)
      print(f"Welcome {user.nickname}")
      time.sleep(5)
      limpa()
      esc1 = int(input("2. Criar carteira? "))
      if esc1 == 2:
        create_wallet(user)
      else:
        print_wallets(user)


  elif esc == 2:
    if user_authentication(user) == 1 and passwd_authentication(user) == 1:
      print(f"Welcome {user.nickname}")
      time.sleep(5)
      limpa()
      esc1 = int(input("2. Criar carteira? "))
      if esc1 == 2:
        create_wallet(user)
      else:
        print_wallets(user)
        

    elif user_authentication(user) == 0:
      print("Usuário não existe!")
    else:
      print("Alguma coisa errada aconteceu!\n")

  return user


# MAIN
esc = int(input("1. Sign Up\n2. Log in\nEnter: "))
limpa()
user = user_account()
authenticator(esc, user)

print(user.wallets)