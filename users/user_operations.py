import getpass
from users.user import User
from utils.file_operations import save_user_info, load_user_info, load_user_passwd
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
            print(f"Welcome {user.nickname}")
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
