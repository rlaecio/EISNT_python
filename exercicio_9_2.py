import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear') or None

limpar()
print("\n Bem-vindo --------------- ")
valor_1 = input('\n Digite o primeiro numero: ')

limpar()
valor_2 = input('\n Digite o segundo numero: ')

limpar()
valor_3 = input('\n Digite o terceiro numero: ')

limpar()
print('\n O maior valor entre os tres numeros é o ', end=''),
if (valor_1 > valor_2 and valor_1 > valor_3):
   print(valor_1, '= valor 1')
elif (valor_2 > valor_1 and valor_2 > valor_3):
   print(valor_2, '= valor 2')
elif (valor_3 > valor_2 and valor_3 > valor_1):
   print(valor_3, '= valor 3')
else:
   print('Algo inesperado aconteceu') 

