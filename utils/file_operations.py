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
            file.write(f"- Nome da Carteira: {wallet.nome}\n")
            file.write(f"  Tickets: {', '.join(wallet.indices)}\n")
        file.write("\n")

# NOVAS FUNÇÕES
def salva_informacoes_usuario(user):
    with open("db/user_info.txt", "a") as file:
        file.write(f"User [{user.email}] ID: {user.id_usuario}\n")

    with open(f"db/{user.id_usuario}.txt", "w") as file:
        file.write(f"Essa carteira pertence a {user.email}\n")
        file.write(f"Nome: {user.nome}\n")
        file.write(f"Senha: {user.senha}\n")
        
def carrega_id_usuario(email):
    with open("db/user_info.txt", "r") as file:
        for line in file:
            if line.startswith(f"Usuario [{email}] ID: "):
                return line.split(":")[1].strip()
    return None

def carrega_nome_usuario(id_usuario):
    with open(f"db/{id_usuario}.txt", "r") as file:
        for line in file:
            if line.startswith("Nome: "):
                return line.split(":")[1].strip()
    return None

def carrega_senha_usuario(id_usuario):
    with open(f"db/{id_usuario}.txt", "r") as file:
        for line in file:
            if line.startswith("Senha: "):
                return line.split(":")[1].strip()
    return None

def carrega_informacoes_usuario():
    id = carrega_id_usuario()
    nome = carrega_nome_usuario()
    senha = carrega_senha_usuario()
    
    return id, nome, senha
    
def salva_carteira_do_usuario(user):
    with open(f"db/{user.id_usuario}.txt", "a") as file:
        for carteira in user.carteiras:
            file.write(f"- Carteira: {carteira.nome}\n")
            file.write(f"  Tickets: {', '.join(carteira.indices)}\n")
        file.write("\n")