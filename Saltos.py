from sys import argv, exit

def recursao_simples(caminho, posicao, ultimo_salto_de_tres):
    # Caso base: chegou na última posição
    if posicao == len(caminho) - 1:
        return 1

    saltos = 0

    # Salto de 1 metro
    if posicao + 1 < len(caminho) and caminho[posicao + 1] == '1':
        saltos += recursao_simples(caminho, posicao + 1, False)

    # Salto de 2 metros
    if posicao + 2 < len(caminho) and caminho[posicao + 2] == '1':
        saltos += recursao_simples(caminho, posicao + 2, False)

    # Salto de 3 metros (se o último não foi de 3 metros)
    if not ultimo_salto_de_tres and posicao + 3 < len(caminho) and caminho[posicao + 3] == '1':
        saltos += recursao_simples(caminho, posicao + 3, True)

    return saltos

def recursao_memorizada(caminho, posicao, ultimo_salto_de_tres, cache):
    chave = (posicao, ultimo_salto_de_tres)
    if chave in cache:
        return cache[chave]

    # Caso base: chegou na última posição
    if posicao == len(caminho) - 1:
        return 1

    saltos = 0

    # Salto de 1 metro
    if posicao + 1 < len(caminho) and caminho[posicao + 1] == '1':
        saltos += recursao_memorizada(caminho, posicao + 1, False, cache)

    # Salto de 2 metros
    if posicao + 2 < len(caminho) and caminho[posicao + 2] == '1':
        saltos += recursao_memorizada(caminho, posicao + 2, False, cache)

    # Salto de 3 metros (se o último não foi de 3 metros)
    if not ultimo_salto_de_tres and posicao + 3 < len(caminho) and caminho[posicao + 3] == '1':
        saltos += recursao_memorizada(caminho, posicao + 3, True, cache)

    cache[chave] = saltos
    return saltos

def naoRecursao(caminho):
    n = len(caminho)
    dp = [0] * n
    dp[0] = 1  # Começamos na primeira pedra

    for i in range(1, n):
        if caminho[i] == '1':
            # Salto de 1 metro
            dp[i] += dp[i - 1] if i - 1 >= 0 and caminho[i - 1] == '1' else 0
            # Salto de 2 metros
            dp[i] += dp[i - 2] if i - 2 >= 0 and caminho[i - 2] == '1' else 0
            # Salto de 3 metros (se o último não foi de 3 metros)
            if i - 3 >= 0 and caminho[i - 3] == '1':
                dp[i] += dp[i - 3]
                if i - 4 >= 0 and caminho[i - 4] == '1':  # Verifica a restrição de dois saltos consecutivos de 3 metros
                    dp[i] -= dp[i - 4]

    return dp[n - 1]

if __name__ == "__main__": 
    if len(argv) != 2:
        print("Uso: python Saltos.py <saltos>")
        exit(1)

    saltos = argv[1]

    rs = recursao_simples(saltos, 0, False)
    
    cache = {}
    rm = recursao_memorizada(saltos, 0, False, cache)
    
    nr = naoRecursao(saltos)

    print("Recursão Simples: existem", rs)
    print("Recursão Memorizada: existem", rm)
    print("Sem recursão: existem", nr)
