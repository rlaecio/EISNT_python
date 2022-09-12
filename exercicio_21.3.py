import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear') or None
 
def valida_idade():
    limpar()  
    while True:    
        try:          
          while True:
            idade = int(input('Informe a idade : '))  
            if(idade < 17 or idade > 77): 
                raise
            else:
                break
        except ValueError:
            limpar()  
            print('são aceitos apenas numeros ')
        except:
            limpar()  
            print('Idade invalida ')
        else:
            break

   
# inicio do sistema    
valida_idade()
