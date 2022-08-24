import time
import os


def limpar():
    os.system('cls' if os.name == 'nt' else 'clear') or None


limpar()
for i in range(1, 101, 2):
    if i % 3 != 0:
        print(i)
