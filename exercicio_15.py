import os


def limpar():
    os.system('cls' if os.name == 'nt' else 'clear') or None


quantidade = 0
for i in range(1, 11):
    limpar()
    print('\n Informe a idade da', i, 'ª pessoa : ', end=''),
    idade = int(input())
    if idade >= 18:
        quantidade = quantidade + 1

limpar()
print(' Foram', quantidade, 'pessoas, maiores de 18 anos! \n')
