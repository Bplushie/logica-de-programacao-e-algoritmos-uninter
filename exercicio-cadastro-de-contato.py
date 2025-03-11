def menu_validacao():
    """Imprime o menu inicial e também valida o valor int"""
    while True:
        try:
            print(f"{'-'*14} Bem-vindos à lista de contatos de Mariane Okimoto  {'-'*14}")
            print(f"{'-'*37} MENU {'-'*37}")
            print('1)   Cadastrar Contato')
            print('2)   Consultar Contato(s)')
            print('3)   Remover Contato')
            print('4)   Encerrar Programa\n')

            menu = int(input('Escolha um item do menu: '))  # Valor com ponto flutuante
            break  # Sai do loop se os valores forem válidos
        except ValueError:
            print('Erro: Insira um valor válido.')
    return menu #retorna um valor inteiro 

def cadastrar_contato (id):
    """Função padrão de cadastro do contato. Imprime o menu, pergunta os dados e armazena em uma lista"""
    print(f"{'-'*80}")
    print(f"{'-'*30} CADASTRAR CONTATO {'-'*31}")
    print('Novo cadastro de contato:')
    print(f'Id do contato: {id}')
    nome = input("Digite o nome do contato: ")
    atividade = input("Digite a atividade do contato: ")
    telefone = input("Digite o telefone do contato: ")

    contato = {
    'id' : id,
    'nome' : nome,
    'atividade' : atividade,
    'telefone' : telefone,
    }
    
    lista_contatos.append(contato.copy()) 
    print("\nContato Cadastrado com sucesso!\n")

def consultar_contatos():
    """Função de consulta de contatos que permite consultar todos, por id, por atividade ou retornar ao menu."""
    while True:
        try:
            print(f"{'-'*80}")
            print(f"{'-'*30} Consultar contato {'-'*31}")
            print('1) Consultar Todos os contatos')
            print('2) Consultar por Id')
            print('3) Consultar por Atividade')
            print('4) Retornar ao menu\n')
            menu_consulta = int(input('Escolha um item do menu: '))
            print(f"{'-'*80}")

            if menu_consulta == 1:  # Consultar todos os contatos
                if lista_contatos:
                    for contato in lista_contatos:
                        print(f"ID: {contato['id']}\nNome: {contato['nome']}\nAtividade: {contato['atividade']}\nTelefone: {contato['telefone']}\n")
                else:
                    print("Nenhum contato cadastrado.\n") 
            elif menu_consulta == 2:  # Consultar por Id
                try:
                    id_input = int(input('Digite o Id do contato: '))
                    match_encontrado = False
                    for contato in lista_contatos:
                        if contato['id'] == id_input:
                            print(f"ID: {contato['id']}\nNome: {contato['nome']}\nAtividade: {contato['atividade']}\nTelefone: {contato['telefone']}\n")
                            match_encontrado = True
                            break
                    if not match_encontrado:
                        print('Id não encontrado.\n')
                except ValueError:
                    print("Erro: Digite um número válido.\n")
            elif menu_consulta == 3:  # Consultar por Atividade
                atividade_input = input('Digite a atividade do contato: ')
                contatos_encontrados = False
                for contato in lista_contatos:
                    if contato['atividade'].lower() == atividade_input.lower():
                        print(f"ID: {contato['id']}\nNome: {contato['nome']}\nAtividade: {contato['atividade']}\nTelefone: {contato['telefone']}\n")
                        contatos_encontrados = True
                if not contatos_encontrados:
                    print('Nenhum contato encontrado para a atividade informada.\n') 
            elif menu_consulta == 4:  # Retornar ao menu principal
                print('Retornando ao menu principal...\n')
                return  # Sai da função e retorna ao menu principal
            else:  # Opção inválida
                print('Opção inválida. Tente novamente.\n') 
        except ValueError:
            print('Erro: Insira um valor válido.\n')

def remover_contato ():
    """Remove o usuário baseado no id e valida o input int"""
    while True:
        try:
            id_input = int(input('Digite o Id do contato que deseja remover: '))
            match_remove_id = False
            for contato in lista_contatos:
                if contato['id'] == id_input:
                    match_remove_id = True
                    lista_contatos.remove(contato)
                    print("\nContato Removido com sucesso!\n")
                    return  
            if not match_remove_id:
                print('Id não encontrado.')
                continue
        except ValueError:
            print("Digite apenas números. Tente novamente.\n")
            continue
        

# -------- Programa principal -------- 

id_global = 5017444
lista_contatos = [] #Lista de armazenamento dos contatos em formato de discionário

while True:
    menu = menu_validacao() # Menu inicial e input do menu
    if menu == 1: 
        id_global += 1
        cadastrar_contato(id_global) 
    elif menu == 2: 
        consultar_contatos ()
    elif menu == 3: 
        remover_contato ()
    elif menu == 4: 
        print('Encerrando o sistema...')
        break
    else:
        print('Insira um número válido.') 
        continue
