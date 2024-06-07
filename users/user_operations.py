import getpass
from users.user import User
from utils.file_operations import salva_informacoes_usuario, carrega_id_usuario, carrega_senha_usuario
from utils.console_operations import limpa
import time

def user_account():
    nickname = str(input("Entre com nome de usuário: "))
    password = getpass.getpass("Sua senha: ")
    user = User(nickname, password)
    return user

def create_account(user):
    save_user_info(user)
    print("Usuário criado\n")
    time.sleep(5)
    limpa()

def passwd_authentication(user):
    user_id = load_user_info(user)
    if user_id:
        user.user_id = user_id
        passwd = load_user_passwd(user_id)
        if user.passwd == passwd:
            return True
    print("Senha incorreta!")
    return False

def user_authentication(user):
    return load_user_info(user) is not None

def authenticator(esc, user):
    from wallets.wallet_operations import create_wallet, print_wallets

    if esc == 1:
        if user_authentication(user):
            print("Usuário já existe")
        else:
            create_account(user)
            print(f"Bem-vindo {user.nickname}")
            time.sleep(5)
            limpa()
            if int(input("2. Criar carteira? ")) == 2:
                create_wallet(user)
            else:
                print_wallets(user)

    elif esc == 2:
        if user_authentication(user) and passwd_authentication(user):
            print(f"Welcome {user.nickname}")
            time.sleep(5)
            limpa()
            if int(input("2. Criar carteira? ")) == 2:
                create_wallet(user)
            else:
                print_wallets(user)
        else:
            print("Usuário não existe ou senha incorreta!")
    else:
        print("Alguma coisa errada aconteceu!\n")

    return user

# NOVAS FUNÇÕES
def criacao_do_usuario():
    email = str(input("Entre com o email:"))
    name = str(input("Seu nome: "))
    password = getpass.getpass("Sua senha: ")
    user = User(email, name, password)
    
    if autentifica_usuario(email):
        salva_informacoes_usuario(user)
        print("Usuário criado\n")
        time.sleep(5)
        limpa()
    print("Usuário já existente")

def conta_do_usuario():
    from utils.file_operations import carrega_nome_usuario
    
    email = str(input("Entre com o email:"))
    nome = carrega_nome_usuario(email)
    senha = getpass.getpass("Sua senha: ")
    user = User(email, nome, senha)
    return user

def atuentifica_senha(user):
    from utils.file_operations import carrega_senha_usuario
    id_usuario = carrega_id_usuario(user.email)
    senha = carrega_senha_usuario(id_usuario)
    
    if user.senha == senha:
        return True
    print("Senha incorreta!")
    return False

def autentifica_usuario(email):
    return carrega_id_usuario(email) is not None
    
    
    
# NOVAS FUNÇÕES - Com Exceções
def criacao_do_usuario():
    try:
        email = input("Entre com o email: ").strip()
        name = input("Seu nome: ").strip()
        password = getpass.getpass("Sua senha: ").strip()
        
        if not email or not name or not password:
            raise ValueError("Todos os campos são obrigatórios.")
        
        user = User(email, name, password)
        
        if autentifica_usuario(email):
            print("Usuário já existente")
        else:
            salva_informacoes_usuario(user)
            print("Usuário criado\n")
            time.sleep(2)
            limpa()
    except ValueError as ve:
        print(f"Erro: {ve}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")