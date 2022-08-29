import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear') or None

def divisores(dividendo):
    divisores = 0
    for i in range(1, dividendo + 1):
        if (dividendo % i) == 0:
            divisores += 1
    return divisores

limpar()
dividendo = int(input('Informe o valor de N : '))

while (dividendo != 9999):
    limpar()
    print('O numero', dividendo, 'possui', divisores(dividendo), 'divisores!')
    dividendo = int(input('\n\nInforme o valor de N : '))



