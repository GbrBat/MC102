# MC102W - 1s2020
# Aluno: Gabriel Batista
# RA: 212845
# Data: 19/05/2020
# Descrição: Jogo da Vida

linhas = int(input())
colunas = int(input())
iteracoes = int(input())
quant_cel = int(input())
n = 0
x = 0


def ImprimeMatriz(matriz):
    for i in range(1, len(matriz)-1):
        for j in range(1, len(matriz[i])-1):
            print("." if matriz[i][j] == 0 else "+", end='')
        print()
    print("-")
    return

def CriaMatriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz


matriz1 = CriaMatriz(linhas + 2, colunas + 2)


while n < quant_cel:
    operacao = input().split(',')
    matriz1[int(operacao[0])+1][int(operacao[1])+1] = 1
    n += 1

ImprimeMatriz(matriz1)

while x < iteracoes:
    matriz2 = CriaMatriz(linhas + 2, colunas + 2)
    for i in range(1, len(matriz1) - 1):
        for j in range(1, len(matriz1[i]) - 1):
            vizinho1 = matriz1[i - 1][j - 1]
            vizinho2 = matriz1[i - 1][j]
            vizinho3 = matriz1[i - 1][j + 1]
            vizinho4 = matriz1[i][j - 1]
            vizinho5 = matriz1[i][j + 1]
            vizinho6 = matriz1[i + 1][j - 1]
            vizinho7 = matriz1[i + 1][j]
            vizinho8 = matriz1[i + 1][j + 1]
            quantidade_vivos = vizinho1 + vizinho2 + vizinho3 + vizinho4 + vizinho5 + vizinho6 + vizinho7 + vizinho8
            if matriz1[i][j] == 0:
                if quantidade_vivos == 3:
                    matriz2[i][j] = 1
            else:
                if quantidade_vivos == 2 or quantidade_vivos == 3:
                    matriz2[i][j] = 1
    matriz1 = matriz2
    ImprimeMatriz(matriz1)
    x += 1









