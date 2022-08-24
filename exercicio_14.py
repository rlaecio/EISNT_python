import time
import os


def limpar():
    os.system('cls' if os.name == 'nt' else 'clear') or None


limpar()
for i in range(1, 101):
    if i % 2 == 0 and i % 3 != 0:
        print(i)
