from random import randint
def diferenca_absoluta_matriz():
    global matriz
    global n
    n = int(input("Número de linhas e colunas: "))
    matriz = [0] * n
    for linha in range(n):
        matriz[linha] = [0] * n
    for linha in range(n):
        for coluna in range(n):
            matriz[linha][coluna] = randint(0,30)
    for linha in range(n):
        print(matriz[linha])
    armazena_diagonal_esquerda = 0
    for diagonalE in range(n):    
        armazena_diagonal_esquerda = matriz[diagonalE][diagonalE] + armazena_diagonal_esquerda
    armazena_diagonal_direita = 0
    inversa = 0
    for diagonalD in range(n-1,-1,-1):
        armazena_diagonal_direita = matriz[inversa][diagonalD] + armazena_diagonal_direita
        inversa += 1
    diferenca_absoluta = armazena_diagonal_esquerda - armazena_diagonal_direita
    if diferenca_absoluta < 0:
        print(f"A diferença absoluta das diagonais é {diferenca_absoluta*-1}")
    else:
        print(f"A diferença absoluta das diagonais é {diferenca_absoluta}")
diferenca_absoluta_matriz()

