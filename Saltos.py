from sys import argv, exit

def recursaoSimples(saltos : str, n : int):
    cont = 0
    saltos = saltos[n:]
    if(saltos!='m'):
        recursaoSimples(saltos, n)
        cont += 1
    else:
        return cont

                

if __name__ == "__main__": #Usar o algoritmo pelo console
    if len(argv) != 2:
        print("Uso: python Saltos.py <saltos>")
        exit(1)
        
    saltos = argv[1]
    
    s = recursaoSimples(saltos, 1)
    
    print("Resultado:", s)