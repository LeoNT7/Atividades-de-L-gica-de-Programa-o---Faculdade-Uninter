print("Bem-vindo a Empresa Leonardo Bento!") 
print("-----------------------------------------------------------") 
 
lista_funcionarios = [] 
id_global = 5438696 #id global com meu ru 
 
# Função para cadastrar funcionário 
def cadastrar_funcionario(id): 
    print("----------- MENU CADASTRAR FUNCIONÁRIO ----------------") 
    print(f"Id do Funcionário: {id}") 
    nome = input("Nome do Funcionário: ") 
    setor = input("Por favor entre com o setor do funcionário: ") 
    salario = float(input("Por favor entre com o salário do funcionário: ")) 
    funcionario = { 
        "id": id, 
        "nome": nome, 
        "setor": setor, 
        "salario": salario 
    } 
    lista_funcionarios.append(funcionario.copy()) 
    print("-----------------------------------") 
    print("Funcionário cadastrado com sucesso!") 
    print("-----------------------------------") 
 
# Função para consultar funcionários 
def consultar_funcionarios(): 
    while True: 
        print("--------- MENU CONSULTAR FUNCIONÁRIO ------------") 
        print("1. Consultar Todos") 
        print("2. Consultar por Id") 
        print("3. Consultar por Setor") 
        print("4. Retornar ao menu") 
        opcao = input("Escolha uma opção: ") 
 
        if opcao == "1": 
            for f in lista_funcionarios: #itera sobre toda a lista 
                print(f) 
        elif opcao == "2": 
            id_consulta = int(input("Informe o ID: ")) 
            encontrado = False #começa como falso 
            for f in lista_funcionarios: #itera sobre a lista 
                if f["id"] == id_consulta: #se localizar o id que foi digitado altera para verdadeiro 
                    print(f) 
                    encontrado = True 
            if not encontrado: #verifica se encontrado é true ou false, se falso executa o print abaixo 
                print("---------------------------") 
                print("Funcionário não encontrado.") 
                print("---------------------------") 
        elif opcao == "3": 
            setor_consulta = input("Informe o setor: ") 
            encontrados = [f for f in lista_funcionarios if f["setor"].lower() == setor_consulta.lower()] 
            if encontrados: 
                for f in encontrados: 
                    print(f) 
            else: 
                print("------------------------------------------") 
                print("Nenhum funcionário encontrado nesse setor.") 
                print("------------------------------------------") 
        elif opcao == "4": 
            return 
        else: 
            print("Opção inválida") 
        print("------------------------------------------------------") 
 
# Função para remover funcionário 
def remover_funcionario(): 
    while True: 
        print("------------- MENU REMOVER FUNCIONÁRIO ---------------") 
        id_remover = int(input("Informe o ID do funcionário a ser removido: ")) 
        for f in lista_funcionarios: 
            if f["id"] == id_remover: 
                lista_funcionarios.remove(f) 
                print("----------------------------------") 
                print("Funcionário removido com sucesso!") 
                print("----------------------------------") 
                return 
        print("Id inválido") 
 
 
# Menu principal 
while True: 
    print("-------------------- MENU PRINCIPAL ----------------------") 
    print("Escolha a opção desejada:") 
    print("1 - Cadastrar Funcionário") 
    print("2 - Consultar Funcionário(s)") 
    print("3 - Remover Funcionário(s)") 
    print("4 - Sair") 
    escolha = input(">>") 
    print("----------------------------------------------------------") 
 
    if escolha == "1": 
        cadastrar_funcionario(id_global) 
        id_global += 1  # Incrementa o ID global 
    elif escolha == "2": 
        consultar_funcionarios() #menu consulta funcionarios 
    elif escolha == "3": 
        remover_funcionario() #Menu remover funcionario 
    elif escolha == "4": 
        print("Programa encerrado.") 
        break #Encerra o programa e o looping wile 
    else: 
        print("Opção inválida") 
 
 

 