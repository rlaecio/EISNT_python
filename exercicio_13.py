import time
import os


def limpar():
    os.system('cls' if os.name == 'nt' else 'clear') or None


limpar()
for i in range(100, 0, -1):
    time.sleep(.5)
    limpar()
    print(i)

print('Concluido com sucesso!!')