import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear') or None


limpar()
print("\n Bem-vindo --------------- ")

valor = int(input('\n Introduza um valor entre 0 e 20: '))
while (valor > 20) or ( valor < 0):
    limpar()
    print('Valor invalido!')

    if( valor > 0):
        print('Notas não podem ser superior a 20!')

    if( valor < 0):
        print('Não são aceitos valores negativos!')

    valor = int(input('\n Introduza um valor entre 0 e 20: '))

    
    
