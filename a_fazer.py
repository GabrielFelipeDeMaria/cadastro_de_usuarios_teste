        # PRIMEIRA ETAPA DO DESAFIO AFL PARA ESTAGIÁRIO, CRIAR UM CÓDIGO ONDE SERÁ FEITO O CADASTRO DE USUÁRIOS:

        #   Para cadastrar um usuário, vc precisa dos seguinte atributos:
        #       - Nome
        #       - Idade
        #       - Sexo
        #       - CPF

        #   Para concluir o cadastro do usuário deves-se respeitar as seguintes regras:
        #       - O CPF deve ser único ou seja somente um CPF por usuário
        #       - Idade deve ser de 12 a 100 anos
        #       - Sexo, só permitido masculino e feminino
        #       - Nome deve ser acima de 4 letras, não é permitido numero
        
        #   O Terminal deverá ter a seguintes opções de ações:
        #       1. Cadastrar um Novo usuário
        #       2. Visualizar Usuários
        #       3. Pesquisar Usuários
        #       4. Atualizar Usuário
        #       5. Deletar Usuário

usuarios = {}

# isdigit(): Verifica se contém apenas números.
# len() == 11: Verifica se tem exatamente 11 dígitos.
# cpf not in usuarios: Verifica se o CPF já foi cadastrado.

def cpf_valido(cpf):
    return cpf.isdigit() and len(cpf) == 11 and cpf not in usuarios

def idade_valida(idade):
    return idade.isdigit() and 12 <= int(idade) <= 100

# isalpha(): Verifica se não contém números.
def nome_valido(nome):
    return len(nome) > 4 and nome.replace(" ", "").isalpha()

# lower(): Faz uma cópia da string com todos os caracteres minúsculos.
def sexo_valido(sexo):
    return sexo.lower() in ["masculino", "feminino"]

def cadastrar_usuario():
    print("\n--- Cadastrar Usuário ---")
    
    nome = input("Nome: ")
    while not nome_valido(nome):
        print("Nome inválido! Deve ter mais de 4 letras e não pode conter números.")
        nome = input("Nome: ")

    idade = input("Idade: ")
    while not idade_valida(idade):
        print("Idade inválida! Deve estar entre 12 e 100 anos.")
        idade = input("Idade: ")

#capitalize(): Transforma o primeiro caractere da string em maiúscula e os demais em minúscula.
    sexo = input("Sexo (Masculino/Feminino): ").capitalize()
    while not sexo_valido(sexo):
        print("Sexo inválido! Digite 'Masculino' ou 'Feminino'.")
        sexo = input("Sexo (Masculino/Feminino): ").capitalize()

    cpf = input("CPF (somente números): ")
    while not cpf_valido(cpf):
        print("CPF inválido ou já cadastrado! Deve conter 11 dígitos.")
        cpf = input("CPF (somente números): ")

    usuarios[cpf] = {"Nome": nome, "Idade": int(idade), "Sexo": sexo}
    print("Usuário cadastrado com sucesso!")

#items(): nos permite acessar de maneira mais fácil as chaves e os valores existentes em um dicionário.
def visualizar_usuarios():
    print("\n--- Lista de Usuários ---")
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for cpf, dados in usuarios.items():
            print(f"CPF: {cpf} | Nome: {dados['Nome']} | Idade: {dados['Idade']} | Sexo: {dados['Sexo']}")

def pesquisar_usuario():
    cpf = input("\nDigite o CPF do usuário: ")
    if cpf in usuarios:
        dados = usuarios[cpf]
        print(f"Usuário encontrado!\nNome: {dados['Nome']} | Idade: {dados['Idade']} | Sexo: {dados['Sexo']}")
    else:
        print("Usuário não encontrado.")

def deletar_usuario():
    cpf = input("\nDigite o CPF do usuário para deletar: ")
    if cpf in usuarios:
        del usuarios[cpf]
        print("Usuário removido com sucesso!")
    else:
        print("Usuário não encontrado.")

def menu():
    while True:
        print("\n✐ Sistema de Cadastro ✉")
        print("1 - Cadastrar Usuário")
        print("2 - Visualizar Usuários")
        print("3 - Pesquisar Usuário")
        print("4 - Deletar Usuário")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            visualizar_usuarios()
        elif opcao == "3":
            pesquisar_usuario()
        elif opcao == "4":
            deletar_usuario()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

menu()
