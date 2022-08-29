import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear') or None

fatorial = 1
limpar()

fator = int(input('\n Informe um numero: '))
fatorado = ''
for i in range(fator, 0, -1):
    fatorial *= i
    fatorado += str(i) 

print(fatorado, '\n')
print(' O fatorial de',fator, 'é', fatorial, '\n')
