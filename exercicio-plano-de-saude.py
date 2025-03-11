def validation():
    """Valida a entrada dos dados valorBase e idade"""
    while True:
        try:
            valorBase = float(input('Insira o valor Base do plano: '))  # Valor com ponto flutuante
            idade = int(input('Insira a idade do cliente: '))  # Idade como número inteiro
            break  # Sai do loop se os valores forem válidos
        except ValueError:
            print('Erro: Insira um valor válido.')
    
    return [valorBase, idade]  # Retorna os valores como lista

# Programa principal
print('Sistema desenvolvido por Mariane Okimoto')
print('Seja bem-vindo!')

dadosClientes = validation() # Aqui foi criado uma variável para pegar os dados da lista

# Acessando os valores da lista
valorBase = dadosClientes[0] # Busca o 1º item da lists (valorBase)
idade = dadosClientes[1] # Busca o 2º Valor

# Filtrar a porcentagem conforme a idade
if 0 <= idade < 19:
    porcentagem = 100
elif 19 <= idade < 29:
    porcentagem = 150
elif 29 <= idade < 39:
    porcentagem = 225
elif 39 <= idade < 49: 
    porcentagem = 240
elif 49 <= idade < 59: 
    porcentagem = 350
elif idade <= 49: 
    porcentagem = 600
else:
    print ('entrada inválida')

valorMensal = valorBase * (porcentagem/100) # Formula do valor mensal

print (f'O valor mensal do plano é de: R$ {valorMensal:.2f}') # Retorna o valor com 2 casas decimais após a virgula para centavos

