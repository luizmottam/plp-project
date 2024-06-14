# PLP-PROJECT

## Membros

Marco Antônio Miranda Costacurta (2212130044); 
Luiz de Aquino Motta Mendes (212130077)

## Descrição

Este projeto é uma aplicação em Python para gerenciamento de usuários e suas carteiras. O projeto permite criar usuários, autenticar-se, criar carteiras e visualizar ou deletar carteiras existentes.

## Estrutura do Projeto

- **db/**: Contém os arquivos de banco de dados utilizados para armazenar informações dos usuários.
  - `user_info.txt`: Armazena informações sobre os usuários.

- **users/**: Contém os módulos relacionados aos usuários.
  - `user_operations.py`: Funções para criar, autenticar e gerenciar contas de usuário.
  - `user.py`: Define a classe `User`.

- **utils/**: Contém funções utilitárias usadas no projeto.
  - `console_operations.py`: Funções para operações no console, como limpar a tela e imprimir títulos.
  - `file_operations.py`: Funções para salvar e carregar informações de arquivos.

- **wallets/**: Contém os módulos relacionados às carteiras dos usuários.
  - `wallet_operations.py`: Funções para criar, visualizar e deletar carteiras.
  - `wallet.py`: Define a classe `Wallet`.

- **main.py**: Ponto de entrada principal do programa.

## Dependências

O projeto depende das seguintes bibliotecas Python:

- `getpass`
- `time`
- `os`
- `uuid`

Essas bibliotecas são todas parte da biblioteca padrão do Python, então você não precisa instalar nada extra.

## Instalação e Execução

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/plp-project
cd plp-project
```

2. Certifique-se de que você tem o Python instalado em sua máquina. Este projeto foi testado com o Python 3.8+.

3. Execute o script principal:

```bash
python main.py
```

## Funcionalidades

### Usuários

- **Criar usuário**: O usuário pode se registrar fornecendo um e-mail, nome e senha.
- **Autenticar usuário**: O usuário pode se autenticar fornecendo seu e-mail e senha.

### Carteiras

- **Criar carteira**: Usuários autenticados podem criar carteiras com um nome e uma lista de índices.
- **Visualizar carteiras**: Usuários autenticados podem visualizar todas as suas carteiras.
- **Deletar carteira**: Usuários autenticados podem deletar uma de suas carteiras.

## Estrutura do Código

### user.py

Define a classe `User` que representa um usuário no sistema.

### user_operations.py

Contém funções para operações relacionadas ao usuário, como criar e autenticar usuários.

### wallet.py

Define a classe `Wallet` que representa uma carteira no sistema.

### wallet_operations.py

Contém funções para operações relacionadas às carteiras, como criar, visualizar e deletar carteiras.

### file_operations.py

Contém funções para salvar e carregar informações de usuários e carteiras a partir de arquivos.

### console_operations.py

Contém funções utilitárias para operações no console, como limpar a tela e imprimir títulos.

### main.py

Contém a lógica principal do programa, incluindo o menu de login e o menu de operações das carteiras.

## Contribuição

Se você quiser contribuir com o projeto, por favor, faça um fork do repositório e envie um pull request com suas alterações. Sinta-se à vontade para abrir issues para relatar bugs ou sugerir melhorias.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.
