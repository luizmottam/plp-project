def save_user_info(user):
    with open("db/user_info.txt", "a") as file:
        file.write(f"User [{user.nickname}] ID: {user.user_id}\n")

    with open(f"db/{user.user_id}.txt", "w") as file:
        file.write(f"Essa carteira pertence a {user.nickname}\n")
        file.write(f"Passwd: {user.passwd}\n")

def load_user_info(user):
    with open("db/user_info.txt", "r") as file:
        for line in file:
            if line.startswith(f"User [{user.nickname}] ID: "):
                return line.split(":")[1].strip()
    return None

def load_user_passwd(user_id):
    with open(f"db/{user_id}.txt", "r") as file:
        for line in file:
            if line.startswith("Passwd: "):
                return line.split(":")[1].strip()
    return None

def save_user_wallets(user):
    with open(f"db/{user.user_id}.txt", "a") as file:
        for wallet in user.wallets:
            file.write(f"- Wallet Name: {wallet.nome}\n")
            file.write(f"  Tickets: {', '.join(wallet.indices)}\n")
        file.write("\n")
