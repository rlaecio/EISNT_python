import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear') or None

def bissexto(ano):
    return (ano % 4==0 and ano % 100 != 0) or (ano % 400==0)
        
def dias_contados(ano_nascimento):
    ano_fim = 2022
    dias_totais = 0
    for x in range(ano_nascimento, ano_fim):
        if bissexto(ano_nascimento):
           dias_totais += 366
        else:
           dias_totais += 365    
    return dias_totais

limpar()
ano_nascimento = int(input('Digite o ano de nascimento: '))
     
print('Foram', dias_contados(ano_nascimento), 'dias vividos')


