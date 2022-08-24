import os
os.system('cls') or None

print("\n Bem-vindo --------------- ")
valor_1 = float(input('\n Digite o valor 1: '))

os.system('cls') or None
valor_2 = float(input('\n Digite o valor 2: '))

os.system('cls') or None
valor_3 = float(input('\n Digite o valor 3: '))

os.system('cls') or None
maior = valor_1
menor = valor_1

if (valor_2 > maior):  maior = valor_2
if (valor_3 > maior):  maior = valor_3   

if (valor_2 < menor):  menor = valor_2
if (valor_3 < menor):  menor = valor_3   

print('O maior valor é', maior, 'O menor valor é', menor)