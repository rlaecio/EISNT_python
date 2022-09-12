import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear') or None

limpar()
cidade = ["Aveiro", "Braga", "Braganca", "Regua"]  
 
print(cidade) 
cidade_remover = input('Defina a cidade a substituir: ')

indice = int(cidade.index(cidade_remover.capitalize()))
cidade[indice] = "Porto"

print('\nNova lista :', cidade)

