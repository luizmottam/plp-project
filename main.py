from users.user_operations import user_account, authenticator
from utils.console_operations import limpa

def main():
    esc = int(input("1. Sign Up\n2. Log in\nEnter: "))
    limpa()
    user = user_account()
    authenticator(esc, user)
    print(user.wallets)

if __name__ == "__main__":
    main()
