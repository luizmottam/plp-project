# NOVAS FUNÇÕES
def salva_informacoes_usuario(user):
    with open("db/user_info.txt", "a") as file:
        file.write(f"Usuario [{user.email}] ID: {user.id_usuario}\n")

    with open(f"db/{user.id_usuario}.txt", "w") as file:
        file.write(f"Essa carteira pertence a {user.email}\n")
        file.write(f"Nome: {user.nome}\n")
        file.write(f"Senha: {user.senha}\n")
        
def carrega_id_usuario(email):
    try:
        with open("db/user_info.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line.startswith(f"Usuario [{email}] ID:"):
                    return line.split(": ")[1].strip()
    except FileNotFoundError:
        print("Arquivo user_info.txt não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao carregar o ID do usuário: {e}")
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
        carteira = user.carteiras[len(user.carteiras) - 1]
        file.write(f"- Carteira: {carteira.nome}\n")
        # Formata os tickets removendo espaços extras e caracteres não desejados
        tickets_formatados = [ticket.strip() for ticket in carteira.indices.split(',')]
        # Remove itens vazios da lista
        tickets_formatados = [ticket for ticket in tickets_formatados if ticket]
        file.write(f"  Tickets: {', '.join(tickets_formatados)}\n")
        carteira = None
        file.write("\n")
        
