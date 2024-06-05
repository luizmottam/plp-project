from Usuario import Usuario
from Scripts.Services.CarteriaService import CarteiraService

def main():
    # Criando um usuário
    usuario = Usuario(nome="João Silva", email="joao@example.com")
    
    # Criando uma carteira para o usuário
    carteira = CarteiraService.criar_carteira_para_usuario(usuario, "Carteira de Investimentos")
    
    # Adicionando tickets à carteira
    CarteiraService.adicionar_ticket_na_carteira(carteira, "AAPL")
    CarteiraService.adicionar_ticket_na_carteira(carteira, "GOOGL")
    
    # Exibindo o usuário e suas carteiras
    print(usuario)

if __name__ == "__main__":
    main()
