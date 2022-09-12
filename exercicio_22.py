import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear') or None


limpar()

equipa=["Antonio", "Ana", "Teresa", "Telmo", "João", "Guilherme", "Luis"]   

equipa.sort(reverse=True)
print(equipa) 
