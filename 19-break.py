# código infinito com break 

condicao = True

while condicao:
    nome = input("qual seu nome?: ")

    if nome == 'sair':
        break # para execução do while, sai do loop de repetição

    print(f"seu nome é: {nome}")

    print('acabou!')
