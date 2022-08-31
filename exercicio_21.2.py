import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear') or None

    
def calcula_F():
    try:       
        x = int(input("Introduza o valor de X : "))
        y = int(input("Introduza o valor de y : "))
        resultado = x / (y - 6)
        print(round(resultado, 2))

    except ValueError:
        print("Introduziu uma valor invalido!")
        calcula_F()

    except ZeroDivisionError:
        print("Erro! Impossivel divisão por zero!")
        calcula_F()
    except:
        print("algo ocorreu mau..")


limpar()
calcula_F()