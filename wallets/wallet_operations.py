from wallets.wallet import Wallet
from utils.console_operations import limpa, titulo
from utils.file_operations import salva_carteira_do_usuario
import time

def imprimir_carteira(user):
    try:
        with open(f"db/{user.id_usuario}.txt", 'r') as file:
            lines = file.readlines()
            if len(lines) < 3:
                print("Você ainda não tem nenhuma carteira")
            else:
                titulo("SUAS CARTEIRAS")
                for linha in lines[3:]:
                    print(linha.strip())
    except FileNotFoundError:
        print("Arquivo de carteira não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler a carteira: {e}")

def imprime_nova_carteira(carteira):
    try:
        titulo("CARTEIRA ADICIONADA")
        print(f"- Carteira : {carteira.nome}")
        print(f"  Indices: {carteira.indices}")
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

def deletar_carteira_do_usuario(user):
    try:
        nome_carteira = input("Digite o nome da carteira para ser deletada: ")

        with open(f"db/{user.id_usuario}.txt", "r") as file:
            linhas = file.readlines()

        if not any(line.startswith(f"- Carteira: {nome_carteira}") for line in linhas):
            raise ValueError(f"A carteira '{nome_carteira}' não foi encontrada.")

        novas_linhas = []
        skip = False
        for line in linhas:
            if line.startswith(f"- Carteira: {nome_carteira}"):
                skip = True
                continue
            if skip and line.startswith("- Carteira:"):
                skip = False
            if not skip:
                novas_linhas.append(line)

        result_linhas = [line for i, line in enumerate(novas_linhas) if not (line.strip() == "" and (i == 0 or novas_linhas[i - 1].strip() == ""))]

        with open(f"db/{user.id_usuario}.txt", "w") as file:
            file.writelines(result_linhas)

        print(f"A carteira '{nome_carteira}' foi deletada com sucesso.")
    except ValueError as ve:
        print(f"Erro: {ve}")
    except Exception as e:
        print(f"Ocorreu um erro ao deletar a carteira: {e}")