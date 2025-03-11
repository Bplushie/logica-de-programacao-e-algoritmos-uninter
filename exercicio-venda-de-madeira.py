def escolha_tipo():
    """Pergunta o tipo de madeira e retorna o nome por extenso do tipo de madeira e o valor do metro cúbico"""
    while True:
        tipoMadeira = input('\nQual o tipo de madeira desejada: ').lower() # Aqui converti para minúsculas para que o código leia a entrada tanto em maiúsculo ou minúsculo
        match tipoMadeira: # Tentei utilizar o match case conforme ensinado nas aulas extras 
            case 'pin':
                valorMetro = 150.40
                tipoMadeira = 'Pinho'
                return tipoMadeira, valorMetro
            case 'per':
                valorMetro = 170.20
                tipoMadeira = 'Peroba'
                return tipoMadeira, valorMetro
            case 'mog':
                valorMetro = 190.90 
                tipoMadeira = 'Mogno'
                return tipoMadeira, valorMetro
            case 'ipe': 
                valorMetro = 210.10
                tipoMadeira = 'Ipê'
                return tipoMadeira, valorMetro
            case 'imb':  
                valorMetro = 220.70
                tipoMadeira = 'Imbuia'
                return tipoMadeira, valorMetro
            case _:
                print('Escolha inválida, entre com o modelo novamente.')
                continue 

def qtd_toras():
    """Pergunta a quantidade de toras e retorna essa quantidade e o valor de desconto aplicado"""
    while True: 
        try:
            qtdToras = int(input('Entre com a quantidade de toras (m3): '))

            if qtdToras < 100:
                print ('Ótima escolha!\n')
                valorDesconto = (0/100)
            elif 100 <= qtdToras < 500: 
                print ('Parabéns! Você tem 4% de desconto nessa compra\n')
                valorDesconto = (4/100)
            elif 500 <= qtdToras < 1000: 
                print ('Parabéns! Você tem 9% de desconto nessa compra\n')
                valorDesconto = (9/100)
            elif 1000 <= qtdToras <= 2000: 
                print ('Parabéns! Você tem 16% de desconto nessa compra\n')
                valorDesconto = (16/100)
            elif qtdToras > 2000: 
                print ('Não aceitamos pedidos com essa quantidade de toras\n')
                continue
            else: 
                print ('Não aceitamos pedidos com essa quantidade de toras\n')
                continue
            break
        except ValueError: # Pergunta novamente para o cliente caso ele insira algo diferente de um número inteiro
            print('Selecione uma entrada válida')
            continue
    return qtdToras, valorDesconto
    
def transporte ():
    print('Escolha o tipo de transporte')
    print('1 - Transporte Rodoviário - R$ 1000.00')
    print('2 - Transporte Ferroviário - R$ 2000.00')
    print('3 - Transporte Hidroviário - R$ 2500.00')
    
    while True:
        try:
            tipoTransporte = int(input())

            if tipoTransporte == 1:
                vlrtransporte = 1000
            elif tipoTransporte == 2:
                vlrtransporte = 2000
            elif tipoTransporte == 3:
                vlrtransporte = 2500
            else: 
                print('Selecione uma entrada válida')
                continue
            break
        except ValueError:
            print('Selecione uma entrada válida')
            continue
    return vlrtransporte

# Programa principal
print('Bem vindo a Madeireira da Lenhadora Mariane Okimoto')
print('Entre com o Tipo de Madeira Desejada')
print('PIN - Tora de Pinho')
print('PER - Tora de Peroba')
print('MOG - Tora de Mogno')
print('IPE - Tora de Ipê')
print('IMB - Tora de Imbuia')

# Recebendo os parâmetros das funções e as colocando em variáveis
tipoMadeira, valorMetro = escolha_tipo() 
qtdToras, valorDesconto = qtd_toras()
vlrtransporte = transporte ()

total = ((valorMetro * qtdToras)*(1-valorDesconto)) + vlrtransporte #formula para calculo

print (f'Você escolheu: {qtdToras} x Madeira {tipoMadeira}.\nTotal a pagar: R$ {total:.2f}') 

