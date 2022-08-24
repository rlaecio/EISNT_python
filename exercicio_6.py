import os
os.system('cls') or None

print("\n Bem-vindo --------------- ")

entrada = int(input('\n Digite um numero: '))

resultado = entrada * 12
print('\n O resultado da multiplicação ente', entrada, 'e 12 é :', resultado)
print('\n O numero', resultado, 'possui', len(str(resultado)), 'digito(s)')