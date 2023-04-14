import numpy as np

'''lerGrafo: Usado para ler uma instância'''
def lerGrafo(matriz):
    with open(matriz, 'rb') as f:
        data = np.genfromtxt(f)

    return data


def verificaAdjacencia(matriz, vi, vj):
    # Para encontrar o tamanho quadrático da matriz.
    tamanho = np.shape(matriz)[0]
    # Verifica se existe os vertices na matriz, e se o valor é igual a 0 (que não seria adjacente), retornando false.
    if vi >= tamanho or vj >= tamanho or matriz[vi][vj] == 0:
        return False
    else:
        return True

def tipoGrafo(matriz):
    tipo = '0'
    tipo2 = '0'
    qtd = np.shape(matriz)[0]

    if np.sum(np.diagonal(matriz)) > 0: # Avaliando se é um pseudografo
        tipo2 = '3'
    else:  # Avaliando se é um multigrafo
        for i in range(0, qtd):
            for j in range(0, qtd):
                if matriz[i][j] > 1:
                    tipo2 = '2'
                    break

    for vi in range(0, qtd): # Avaliando se é um grafo simples ou direcionado
        for vj in range(vi + 1, qtd):
            if matriz[vi][vj] == matriz[vj][vi]:
                tipo = '0'
            else:
                tipo = '1'

    res = (int(tipo2 + tipo))
    return res;

def calcDensidade(matriz):

    V = np.shape(matriz)[0] # Representando o número de vértices
    E = np.sum(matriz) # Representando a soma de arestas da matriz
    D = E/(V*(V-1)) # Fórmula para calcular a densidade

    return (round(D,3))

def insereAresta(matriz, vi, vj):
    tipo = '0'
    qtd = np.shape(matriz)[0]

    # Verificando se é um grafo simples ou direcionado
    for i in range(0, qtd):
        for j in range(i + 1, qtd):
            if matriz[i][j] != matriz[j][i]:
                tipo = '1'
                break

    # Inserindo a aresta na matriz de adjacência
    if tipo == '0':
        matriz[vi][vj] += 1
        matriz[vj][vi] += 1
    else:
        matriz[vi][vj] += 1

    return matriz

def insereVertice(matriz):

    qtd = np.shape(matriz)[0]
    matriz2 = np.zeros((qtd + 1, qtd + 1), dtype=int) # np.zeros é usado para preencher com zeros as linhas e colunas
    matriz2[:qtd, :qtd] = matriz # Aqui eu copio a antiga matriz nesta nova

    return matriz2

def removeAresta(matriz, vi, vj):
    tipo = '0'
    qtd = np.shape(matriz)[0]

    # Verificando se é um grafo simples ou direcionado
    for i in range(0, qtd):
        for j in range(i + 1, qtd):
            if matriz[i][j] != matriz[j][i]:
                tipo = '1'
                break

    # Inserindo a aresta na matriz de adjacência
    if tipo == '0':
        matriz[vi][vj] = matriz[vi][vj]-1
        matriz[vj][vi] = matriz[vj][vi]-1
    else:
        matriz[vi][vj] = matriz[vi][vj]-1

    return matriz

def removeVertice(matriz, vi):
    qtd = np.shape(matriz)[0]

    matriz2 = np.array(matriz)

    for i in range(qtd):
        matriz2[vi][i] = -1
        matriz2[i][vi] = -1

    return matriz2





















