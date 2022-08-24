import os
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear') or None

limpar()
print("\n Bem-vindo --------------- ")


nome = input('\n Introduza o nome : ')
# validação do tamanho do nome
while (len(nome) < 3):
    print(' Nome deve possuir mais de 03 caracteres!')      
    nome = input('\n Introduza o nome : ')


idade = int(input('\n Informe a idade : ')) 
# validação  da idade
while (idade < 0) or (idade > 100):
    if(idade > 100):
        print(idade, ' é muito velho para se cadastar')
    if(idade < 0):
        print(' Não é possivel haver idades negativas!')      
    idade = int(input('\n Informe a idade : ')) 


salario = float(input('\n Informe o salário €: '))
# validação de salario
while (salario < 0):
    print(' O valor do salario não pode ser menor que 0!')      
    salario = float(input('\n Informe o salário €: '))


sexo = input('\n Digite o sexo (M) ou (F) : ').upper()
#validação de sexo
while (sexo !='F' and sexo!='M'):
    print(' Sexo deve ser apenas (M) ou (F)')   
    sexo = input('\n Digite o sexo (M) ou (F) : ').upper()


e_civil = input('\n Informe o estado civil: (C) (S) (v) (D) : ')
#validação de estado civil
while (e_civil.upper() != 'C' and e_civil.upper() != 'C' and e_civil.upper() != 'D' and e_civil.upper() != 'V'):
    print(' Estado civil não valido!') 
    e_civil = input('\n Informe o estado civil: (C) (S) (v) (D) : ')
