#Função exibir menu

def exibirMenu():
    print("CONVERSOR DE TEMPERATURA")
    print("Menu de escolha: ")
    print("1. Converter de Celsius para Fahrenheit")
    print("2. Converter de Celsius para Kelvin")
    print("3. Converter de Fahrenheit para Celsius")
    print("4. Converter de Fahrenheit para Kelvin")
    print("5. Converter de Kelvin para Celsius")
    print("6. Converter de Kelvin para Fahrenheit")
    print("0. Sair")
    escolha = int(input("Escolha uma opção: "))
    return escolha

    #Definição das funções
def Celsius_Fahrenheit(x):
    return 9 * x / 5 + 32

def Celsius_Kelvin(x):
    return x + 273.15

def Fahrenheit_Celsius(x):
    return (x - 32) * 5/9

def Fahrenheit_Kelvin(x):
    return (x - 32) / 1.8 + 273.15

def Kelvin_Celsius(x):
    return x - 273.15
    
def Kelvin_Fahrenheit(x):
    return (x - 273.15) * 1.8 + 32


#Declaração de variáveis
opcao = 7
n1 = 0

while opcao != 0:
    opcao = exibirMenu()

    if opcao in [1,2,3,4,5,6]:
        n1 = float(input("Digite o valor escolhido: "))

    if opcao == 1:
        print(f"A conversão de Celsius para Fahrenheit é: {Celsius_Fahrenheit(n1)}")

    elif opcao == 2:
        print(f"A conversão de Celsius para Kelvin é: {Celsius_Kelvin(n1)}")

    elif opcao == 3:
        print(f"A conversão de Fahrenheit para Celsius é: {Fahrenheit_Celsius(n1)}")

    elif opcao == 4:
        print(f"A conversão de Fahrenheit para Kelvin é: {Fahrenheit_Kelvin(n1)}")

    elif opcao == 5:
        print(f"A conversão de Kelvin para Celsius é: {Kelvin_Celsius(n1)}")

    elif opcao == 6:
        print(f"A conversão de Kelvin para Fahrenheit é: {Kelvin_Fahrenheit(n1)}")

    elif opcao == 0:
        print("Até mais!!!")

    else:
        print("Opcão invávila. Tente novamente.")                        
