from sys import argv, exit

def contar_saltos(caminho, pos, pode_pular_tres):
    # Caso base
    if pos == len(caminho) - 1:
        return 1
    # Inicializa o total de maneiras como 0
    total_maneiras = 0

    # Verifica se é possível pular uma, duas ou três posições e se chegou ao final do caminho
    if pos + 1 < len(caminho) and (caminho[pos + 1] == '1' or caminho[pos + 1] == 'm'):
        # Chama a função recursivamente para a próxima posição
        total_maneiras += contar_saltos(caminho, pos + 1, True)
    
    if pos + 2 < len(caminho) and (caminho[pos + 2] == '1' or caminho[pos + 2] == 'm'):
        total_maneiras += contar_saltos(caminho, pos + 2, True)
    
    if pode_pular_tres and pos + 3 < len(caminho) and (caminho[pos + 3] == '1' or caminho[pos + 3] == 'm'):
        # Passa False para o parâmetro pode_pular_tres para invalidar o pulo de três metros
        total_maneiras += contar_saltos(caminho, pos + 3, False)
    
    return total_maneiras


def contar_saltos_memorizados(caminho, pos, pode_pular_tres, memoria):
    # Caso tenha sido calculado anteriormente, retorna o valor armazenado na memória
    if (pos, pode_pular_tres) in memoria:
        return memoria[(pos, pode_pular_tres)]

    if pos == len(caminho) - 1:
        return 1

    total_maneiras = 0

    if pos + 1 < len(caminho) and (caminho[pos + 1] == '1' or caminho[pos + 1] == 'm'):
        total_maneiras += contar_saltos_memorizados(caminho, pos + 1, True, memoria)
    
    if pos + 2 < len(caminho) and (caminho[pos + 2] == '1' or caminho[pos + 2] == 'm'):
        total_maneiras += contar_saltos_memorizados(caminho, pos + 2, True, memoria)
    
    if pode_pular_tres and pos + 3 < len(caminho) and (caminho[pos + 3] == '1' or caminho[pos + 3] == 'm'):
        total_maneiras += contar_saltos_memorizados(caminho, pos + 3, False, memoria)
    
    memoria[(pos, pode_pular_tres)] = total_maneiras
    return total_maneiras

def calcular_saltos_iterativos(caminho):
    # Inicializa a lista de tuplas de maneiras para cada posição
    maneiras_totais = [(0, 0) for _ in range(len(caminho))]
    # Inicia a primeira posição com 1 maneira de pular
    maneiras_totais[0] = (1, 1)

    for i in range(len(caminho)):
        if caminho[i] == '0':  # Se for um buraco, pula
            continue
        
        # true = maneiras com salto de três metros, false = maneiras sem salto de três metros
        com_tres = maneiras_totais[i][0]  
        sem_tres = maneiras_totais[i][1]

        # Se houver posição anterior, acumula os valores
        if i > 0:
            com_tres += maneiras_totais[i - 1][0]
            sem_tres += maneiras_totais[i - 1][0]
        
        if i > 1:
            com_tres += maneiras_totais[i - 2][0]
            sem_tres += maneiras_totais[i - 2][0]
        
        if i > 2:
            # Se a posição anterior permitir salto de três metros, acumula o valor
            com_tres += maneiras_totais[i - 3][1]

        # Armazena o total de maneiras para a posição atual
        maneiras_totais[i] = (com_tres, sem_tres)
    
    # Retorna o número total de maneiras para a última posição
    return maneiras_totais[-1][0]

if __name__ == "__main__": 
    if len(argv) != 2:
        print("Uso: python Saltos.py <caminho>")
        exit(1)

    caminho = argv[1]

    resultado_simples = contar_saltos(caminho, 0, True)
    resultado_memorizado = contar_saltos_memorizados(caminho, 0, True, {})
    resultado_iterativo = calcular_saltos_iterativos(caminho)

    print("Recursão Simples:", resultado_simples)
    print("Recursão Memorizada:", resultado_memorizado)
    print("Sem recursão:", resultado_iterativo)