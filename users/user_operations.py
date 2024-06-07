import getpass
from users.user import User
from utils.file_operations import salva_informacoes_usuario, carrega_id_usuario, carrega_senha_usuario
from utils.console_operations import limpa
import time
 
# NOVAS FUNÇÕES - Com Exceções
def criacao_do_usuario():
    try:
        email = input("Entre com o email: ").strip()
        name = input("Seu nome: ").strip()
        senha = getpass.getpass("Sua senha: ").strip()
        
        if not email or not name or not senha:
            raise ValueError("Todos os campos são obrigatórios.")
        
        user = User(email, name, senha)
        
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
        
        
def conta_do_usuario():
    from utils.file_operations import carrega_nome_usuario
    
    try:
        email = input("Entre com o email: ").strip()
        id = carrega_id_usuario(email)
        nome = carrega_nome_usuario(id)
        
        if not nome:
            raise ValueError("Usuário não encontrado.")
        
        senha = getpass.getpass("Sua senha: ").strip()
        
        if not senha:
            raise ValueError("Senha não pode ser vazia.")
        
        user = User(email, nome, senha)
        user.id_usuario = carrega_id_usuario(email)
        return user
    except ValueError as ve:
        print(f"Erro: {ve}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return None

def autentifica_senha(user):
    try:
        id_usuario = carrega_id_usuario(user.email)
        
        if not id_usuario:
            raise ValueError("ID de usuário não encontrado.")
        
        senha = carrega_senha_usuario(id_usuario)
        
        if user.senha == senha:
            return True
        else:
            print("Senha incorreta!")
            return False
    except ValueError as ve:
        print(f"Erro: {ve}")
        return False
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return False

def autentifica_usuario(email):
    try:
        return carrega_id_usuario(email) is not None
    except Exception as e:
        print(f"Ocorreu um erro ao autenticar o usuário: {e}")
        return False