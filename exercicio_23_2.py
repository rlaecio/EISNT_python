import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear') or None

limpar()
cidade = ["Aveiro", "Braga", "Porto", "Guimarães", "Lisboa"]   
print(cidade) 
indice = int(input('Defina um indice para excluir a cidade: '))

print('\nRemovido :', cidade[indice])
#cidade.remove(cidade[indice])
cidade.index(indice).remove()

print('\nNova lista :', cidade)
