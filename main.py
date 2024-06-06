from utils.Utils import Utils
from servicos.AuthService import AuthService

def main():
    while True:
        esc = int(input("1. Sign Up\n2. Login\nChoose an option: "))
        usuario = Utils.conta_usuario()
        AuthService.authenticator(esc, usuario)

if __name__ == "__main__":
    main()
