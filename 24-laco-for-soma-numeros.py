# um algoritmo que calcula a soma dos números pares entre 1 e 50

# aline de souza - 2° ano c

soma = 0 

# utilizando o laço for:

for numero in range(1,51):
    if numero % 2 == 0:
        soma += numero 

print(f" a soma dos números pares entre 1 e 50 é: {soma}.")
