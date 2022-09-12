import os
from time import sleep

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear') or None

def lista_():
    limpar()
    print('********** Lista de compras **********')

def escrever():
    lista_()
    f = open("lista.txt", "a")
    texto = input('Insira o texto a ser gravado: ')
    f.write('\n')
    f.write(texto)
    f.close

def ler():
    lista_()
    f = open("lista.txt")
    print(f.read())
    f.close
    input('\n Pressione <ENTER> para continuar')

while True:
    limpar()
    print('********** MENU PRINCIPAL **********')
    print(' 1 - Escrever\n 2 - Ler\n 3 - Sair\n')
    opcao = int(input(' '))
    if (opcao == 1):
        escrever()
    elif(opcao == 2):
        ler()
    elif(opcao == 3):
        print('Saindo ...')
        sleep(2)
        break
    else:
        print('Opção invalida!')
        sleep(1)
        
limpar()



