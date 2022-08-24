import os
os.system('cls') or None

print("\n Bem-vindo --------------- ")
valor_1 = float(input('\n Digite o valor 1: '))

os.system('cls') or None
valor_2 = float(input('\n Digite o valor 2: '))

os.system('cls') or None
valor_3 = float(input('\n Digite o valor 3: '))

os.system('cls') or None
print('\n O maior valor entre os tres numeros é o ', end=''),

if   (valor_1 > valor_2 and valor_1 > valor_3)  :  print(valor_1, '= valor 1')
elif (valor_2 > valor_1 and valor_2 > valor_3)  :  print(valor_2, '= valor 2')
elif (valor_3 > valor_2 and valor_3 > valor_1)  :  print(valor_3, '= valor 3')
else :  print('Algo inesperado ocorreu') 