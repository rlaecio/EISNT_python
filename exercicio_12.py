import os
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear') or None

limpar()
print("\n Bem-vindo --------------- ")


print('\n Introduza o nome : ', end=''), 
nome = input()
# validação do tamanho do nome
while (len(nome) < 3):
    print(' Nome deve possuir mais de 03 caracteres!')      
    print('\n Introduza o nome : ', end=''), 
    nome = input()


print('\n Informe a idade : ', end=''), 
idade = int(input())
# validação  da idade
while (idade < 0) or (idade > 100):
    if(idade > 100):
        print(idade, ' é muito velho para se cadastar')
    if(idade < 0):
        print(' Não é possivel haver idades negativas!')    
    print('\n Informe a idade : ', end=''), 
    idade = int(input()) 


print('\n Informe o salário €: ', end=''), 
salario = float(input())
# validação de salario
while (salario < 0):
    print(' O valor do salario não pode ser menor que 0!')      
    print('\n Informe o salário €: ', end=''), 
    salario = float(input())


print('\n Digite o sexo (M) ou (F) : ', end=''), 
sexo = input().upper()
#validação de sexo
while (sexo !='F' and sexo!='M'):
    print(' Sexo deve ser apenas (M) ou (F)')   
    print('\n Digite o sexo (M) ou (F) : ', end=''), 
    sexo = input().upper()


print('\n Informe o estado civil: (C) (S) (v) (D) : ', end=''), 
e_civil = input()
#validação de estado civil
while (e_civil.upper() != 'C' and e_civil.upper() != 'C' and e_civil.upper() != 'D' and e_civil.upper() != 'V'):
    print(' Estado civil não valido!') 
    print('\n Informe o estado civil: (C) (S) (V) (D) : ', end=''), 
    e_civil = input()