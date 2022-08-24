import os


def limpar():
    os.system('cls' if os.name == 'nt' else 'clear') or None


fatoral = 1
limpar()

fator = int(input('\n Informe um numero para ser fatorado: '))

for i in range(1, fator + 1):
    fatoral *= i
    
print(fatoral)
