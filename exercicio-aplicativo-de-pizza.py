def validation():
    """Valida o sabor e tamanho da pizza"""
    while True:
        sabor = input('\nQual o sabor desejado (PS/PD): ').lower()
        
        if sabor == 'ps' or sabor == 'pd':
            print ('Ótima escolha!')
            break  # Sai do loop se os valores forem válidos
        else:
            print ('Sabor inválido. Tente novamente.')
            continue
    while True:
        tamanho = input('\nQual o tamanho desejado (P/M/G): ').lower()

        if tamanho == 'p' or tamanho == 'm' or tamanho == 'g':
            print ('Anotado!')
            break  # Sai do loop se os valores forem válidos
        else: 
            print ('Não temos esse tamanho. Tente novamente')
            continue
    return [sabor, tamanho]
    
def confirmation (sabor, tamanho):
    """Aqui iremos confirmar o item escolhido do cliente, repetindo o que ele pediu e
    informando o valor a ser pago por esse item"""
    if sabor == 'ps' and tamanho == 'p':
        print('Você escolheu uma Pizza Salgada no tamanho P. Valor: R$ 30,00\n')
        valor = 30
    elif sabor == 'ps' and tamanho == 'm':
        print('Você escolheu uma Pizza Salgada no tamanho M. Valor: R$ 45,00\n')
        valor = 45
    elif sabor == 'ps' and tamanho == 'g':
        print('Você escolheu uma Pizza Salgada no tamanho G. Valor: R$ 60,00\n')
        valor = 60
    elif sabor == 'pd' and tamanho == 'p':
        print('Você escolheu uma Pizza Doce no tamanho P. Valor: R$ 34,00\n')
        valor = 34
    elif sabor == 'pd' and tamanho == 'm':
        print('Você escolheu uma Pizza Doce no tamanho M. Valor: R$ 48,00\n')
        valor = 48
    elif sabor == 'pd' and tamanho == 'g':
        print('Você escolheu uma Pizza Doce no tamanho G. Valor: R$ 66,00\n')
        valor = 66
    else:
        print('Nenhuma pizza selecionada')
        return None
    return valor

def nomeSabor (sabor):
    """Aqui iremos converter os nomes abreviados para nomes em extenso dos sabores"""
    if sabor == 'ps':
        return "Pizza Salgada"
    elif sabor == 'pd':
        return "Pizza Doce"
    
def nomeTamanho (tamanho):
    """Aqui iremos converter os nomes abreviados para nomes em extenso dos tamanhos"""
    if tamanho == 'p':
        return"Pequena"
    elif tamanho == 'm':
        return "Media"
    elif tamanho == 'g':
        return "Grande"

# Programa principal
print(f"{'-'*19} Bem-vindos à Pizzaria da Mariane Okimoto {'-'*19}")
print(f"{'-'*37} MENU {'-'*37}")
print(f"{'-'*5}|     Tamanho     |    Pizza Salgada (PS)    |    Pizza Doce (PD)    |{'-'*5}")
print(f"{'-'*80}")
print(f"{'-'*5}|        P        |        R$ 30,00          |        R$ 34,00       |{'-'*5}")
print(f"{'-'*5}|        M        |        R$ 45,00          |        R$ 48,00       |{'-'*5}")
print(f"{'-'*5}|        G        |        R$ 60,00          |        R$ 66,00       |{'-'*5}")
print(f"{'-'*80}")

# Acessando os valores sobre a pizza:
dadosPizza = validation() # Aqui foi criado uma variável para pegar os dados da lista

sabor = dadosPizza[0] # Busca o 1º item da lists (sabor)
tamanho = dadosPizza[1] # Busca o 2º Valor
saborPizza = nomeSabor(sabor)
tamanhoPizza = nomeTamanho(tamanho)

# Acessando os valores sobre o pedido:
valorTotal = 0 # valor inicial do pedido / acumulador para soma dos valores
pedidos = [] # Lista onde vamos amarzenar os itens

valorTotal += confirmation(sabor,tamanho) # Acrescentando o valor inicial ao pedido
pedidos.append(f'1x {saborPizza} no tamanho {tamanhoPizza}')

# Perguntar se deseja mais alguma coisa
while True:
    algoMais = input('Deseja mais alguma coisa? (S/N):').lower()
    if algoMais == 's':
        dadosPizza = validation()  # Obter novos valores para sabor e tamanho
        sabor = dadosPizza[0] 
        tamanho = dadosPizza[1]
        saborPizza = nomeSabor(sabor)
        tamanhoPizza = nomeTamanho(tamanho)
        valorTotal += confirmation(sabor, tamanho)  # Acrescentando o valor ao total
        pedidos.append(f'1x {saborPizza} no tamanho {tamanhoPizza}')
    elif algoMais == 'n':
        print('Certo!\n')
        break
    else:
        print('Erro! Escolha uma opção válida.')
        continue

# Finalização do pedido
print('PEDIDO REALIZADO:')
for pedido in pedidos:
    print(pedido)
print (f'O Valor total a pagar é: R${valorTotal:.2f}')
