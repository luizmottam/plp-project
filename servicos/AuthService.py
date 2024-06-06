
class AuthService:

    @staticmethod
    def autentificacao_de_senha(user):
        user_id = None
        # Find the user ID
        with open(f"Usuarios/user_info.txt", "r") as file:
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
