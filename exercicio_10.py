import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear') or None


limpar()
print("\n Bem-vindo --------------- ")
categoria = (input('\n Informe a categoria profissional: '))

limpar()
print('\n O salario é de ', end=''),

if   (categoria.upper() == 'A' )    :  print('€ 2500')
elif (categoria.upper() == 'B' )    :  print('€ 2000')
elif (categoria.upper() == 'C' )    :  print('€ 1750')
elif (categoria.upper() == 'D' )    :  print('€ 1250')
elif (categoria.capitalize() == 'Outra' ):  print('€ 750')
else:  
   limpar()
   print('\n  ** Categoria invalida **') 
