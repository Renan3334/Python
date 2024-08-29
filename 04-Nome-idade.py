#Atribuição de variáveis

Nome = "Renan"
Idade = 16
Altura = 1.74

#Exibir mensagem na tela
print(" Nome:", Nome, "| Idade:",Idade, "| Altura:", Altura)
#Formatação com f-string
print(f"Nome: {Nome} | Idade: {Idade} | Altura: {Altura}\n")

Nome = input("Digite o seu nome: ")
Idade = int(input("Digite sua idade: "))
Altura = float(input("Digite a sua altura: "))

print(f"\nNome {Nome}, | Idade {Idade}, | Altura {Altura}")

print("\nObrigado por responder!\n")