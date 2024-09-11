#Elaborar um algoritmo que solicita 4 notas ao usuário.
#O programa deve calcular a média das notas e
#verificar se a média é maior ou igual a 80.
#se a média for maior ou igual a 80, o programa
#deve exibir a mensagem "Aprovado" e se a média for menor que
#80, o programa deve exibir a mensagem "Reprovado"

nota1 = float(input("Digite a nota1: "))
nota2 = float(input("Digite a nota2: "))
nota3 = float(input("Digite a nota3: "))
nota4 = float(input("Digite a nota4: "))

media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"A média final obtida é = {media}")

if (media >= 80):
    print("Aprovado")
else:
    print("Reprovado")