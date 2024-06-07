from wallets.wallet import Wallet
from utils.console_operations import limpa, titulo
from utils.file_operations import salva_carteira_do_usuario
import time

# NOVAS FUNÇÕES - Com Exceções
def imprimir_carteira(user):
    try:
        with open(f"db/{user.id_usuario}.txt", 'r') as file:
            lines = file.readlines()
            if len(lines) < 4:
                print("Você ainda não tem nenhuma carteira")
            else:
                for linha in lines[4:]:
                    print(linha.strip())
    except FileNotFoundError:
        print("Arquivo de carteira não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler a carteira: {e}")
    return 0

def imprime_nova_carteira(carteira):
    try:
        titulo("CARTEIRA ADICIONADA")
        print("- Carteira : ", carteira.nome)
        print("  Indices: ", carteira.indices)
        time.sleep(2)
        limpa()
    except Exception as e:
        print(f"Ocorreu um erro ao imprimir a carteira: {e}")

def criar_carteira(user):
    try:
        titulo("Nova Carteira")
        nome_da_carteira = input("Nome da Carteira: ").strip()
        indices = input("Indices (digite separado por ,): ").strip()

        if not nome_da_carteira:
            raise ValueError("O nome da carteira não pode ser vazio.")
        if not indices:
            raise ValueError("Os índices não podem ser vazios.")

        carteira = Wallet(nome_da_carteira, indices)
        
        while True:
            esc = input("Deseja adicionar carteira a suas carteiras (s/n)? ").strip().upper()
            if esc in ['S', 'N']:
                break
            else:
                print("Opção inválida. Digite 's' para sim ou 'n' para não.")
        
        if esc == 'S':
            user.adicionar_carteira(carteira)
            imprime_nova_carteira(carteira)
            salva_carteira_do_usuario(user)
        else:
            print(f"A carteira {nome_da_carteira} foi descartada")
    except ValueError as ve:
        print(f"Erro: {ve}")
    except Exception as e:
        print(f"Ocorreu um erro ao criar a carteira: {e}")
