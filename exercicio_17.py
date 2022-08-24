import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear') or None

fatorial = 1
limpar()

fator = int(input('\n Informe um numero para ser fatorado: '))
for i in range(1, fator + 1):
    fatorial *= i

print(' O fatorial de',fator, 'é', fatorial, '\n')
