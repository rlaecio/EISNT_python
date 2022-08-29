import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear') or None

def bissexto(ano):
    return (ano % 4==0 and ano % 100 != 0) or (ano % 400==0)
       
def se_bissexto(ano):
    if  (bissexto(ano)):
        print(' O ano de', ano,'é bissexto')
    else:
        print(' O ano de', ano,'não é bissexto')

limpar()
ano = int(input(' Informe o valor do ano do seu nascimento '))

print(se_bissexto(ano))

