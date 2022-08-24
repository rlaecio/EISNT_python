import os


def limpar():
    os.system('cls' if os.name == 'nt' else 'clear') or None

#declarando as variaveis
menor_15, menor_30, menor_45, menor_60, maior_60 = 0, 0, 0, 0, 0

for i in range(1, 16):
    limpar()   

    idade = int(input('\n Informe a idade da '+ str(i)+'ª pessoa : '))
    # valida a idade
    while (idade < 0) or (idade > 100):
        if(idade > 100):
            print(idade, ' é muito velho para se cadastar')
        if(idade < 0):
            print(' Não é possivel haver idades negativas!')  
        idade = int(input('\n Informe a idade da'+ str(i)+'ª pessoa : '))
    
    #calcula as quantidades
    if idade <= 15:
        menor_15 += 1
    elif idade <= 30:
        menor_30 += 1
    elif idade <= 45:
        menor_45 += 1
    elif idade <=60:
        menor_60 += 1
    elif idade > 60:
        maior_60 += 1
   
limpar() #limpa a tela
print('Foram :')
print(menor_15, 'pessoa(s), menores de 15 anos! \n')
print(menor_30, 'pessoas, maiores de 15 e menores de 30 anos! \n')
print(menor_45, 'pessoas, maiores de 30 e menores de 45 anos! \n')
print(menor_60, 'pessoas, maiores de 45 e menores de 60 anos! \n')
print(maior_60, 'pessoas, maiores de 60 anos! \n')
