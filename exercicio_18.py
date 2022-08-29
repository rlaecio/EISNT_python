import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear') or None

def resultado(valor):
    return (valor == 5)
                 
limpar()
valor = int(input(' Digite um valor: '))

print(resultado(valor))
