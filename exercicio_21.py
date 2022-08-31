import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear') or None

def calcular(valor_x, valor_y):
    try:
        res = valor_x / (valor_y - 6)
    except:
        print('Não é possivel calcular o valor')
    else: 
        print('Resultado da equação :', res)    

def calculador():
    limpar()  
    while True:    
        try:          
          while True:
            valor_x = int(input('Informe o valor de X : '))  
            if(valor_x <= 0): 
                raise
            else:
                break
        except:
            limpar()  
            print('Valor invalido, entre com um numero valido')
        else:
            break

    limpar()  
    while True:    
        try:
          while True:
            valor_y = int(input('Informe o valor de Y : '))   
            if(valor_x < 6): 
                raise
            else:
                break
        except:
           print('Valor invalido, entre com um numero valido')
        else:
            break
    
    calcular(valor_x, valor_y)



# inicio do sistema    
calculador()
