import os
os.system('cls') or None

print("\n Bem-vindo --------------- ")
valor_1 = input('\n Digite o primeiro numero:')

os.system('cls') or None
valor_2 = input('\n Digite o segundo numero:')

os.system('cls') or None
print('\n O maior valor entre os dois numeros é o ', end=''),
if (valor_2 > valor_1):
   print(valor_2, ' = valor 2')
else:
   print(valor_1, ' = valor 1') 