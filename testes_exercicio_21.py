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
dividendo = 0
while True:
    if(dividendo != 9999):
        try:
            dividendo = int(input('Informe o valor de N : ')) 
        except:
            print('invalid literal for int() with base 10:')
        else:
            print('O numero', dividendo, 'possui', divisores(dividendo), 'divisores!')
    else:
        break