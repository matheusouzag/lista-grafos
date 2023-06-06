import numpy as np

'''qtdShape: Usado para retornar a quantidade de linhas e colunas'''
def qtdShape(instancia):
    qtd = np.shape(instancia)
    return qtd


'''Salva Resultado: Usado para salvar no arquivos os resultados finais'''
def salvaResultado(resultado):
    stringRes = ''
    for res in resultado:
        stringRes += str(res) + '\n'
    arquivo = open('C:/Users/Matheus Souza/Desktop/faculdade/PERIODO ATUAL/ALGORITMOS EM GRAFOS/atividade 2/Resultados/resultado.txt', 'a+')
    arquivo.writelines(stringRes + '\n')
    arquivo.close()

# Lista
#def criaListaAdjacencias(matriz):
#   listaAdj = {}

#    for i in range(len(matriz)):
#        adj = []
#        for j in range(len(matriz[i])):
#            if matriz[i][j] != 0:
#                for k in range(matriz[i][j]):
#                    adj.append(j)
#        listaAdj[i] = adj

#    return listaAdj

def criaListaAdjacencias(matriz):
    listaAdj = {}  # Dicionário para armazenar a lista de adjacências

    # Converte a matriz para tipo de dado inteiro
    matriz = matriz.astype(int)

    # Percorre a matriz de adjacências e cria a lista de adjacências
    for i in range(len(matriz)):
        adj = []
        for j in range(len(matriz[i])):
            if matriz[i][j] != 0:  # Verifica se o valor é diferente de 0
                # Modificação: Adiciona o vértice j à lista adj apenas uma vez
                for k in range(matriz[i][j]):
                    adj.append(j)
        listaAdj[i] = adj

    return listaAdj
def tipoGrafoLista(listaAdj):
    tipo2 = '0'
    for chave in listaAdj:

        valores = listaAdj[chave]

        if chave in valores:
            tipo2 = '3'
            break
        else:
            for i in listaAdj:
                for j in listaAdj[i]:
                    if listaAdj[i].count(j) > 1:
                        tipo2 = '2'
                        break

    tipo = '0'
    listas = listaAdj.keys()
    for v in listas:
        outros = listaAdj[v]
        for outro in outros:
            if v not in listaAdj[outro]:
                tipo = '1'

    res = (int(tipo2 + tipo))

    return res

def calcDensidadeLista(listaAdj):

    V = len(listaAdj)
    E = 0
    for i in listaAdj:
        qtd = len(listaAdj[i])
        E = E + qtd
    D = E / (V * (V - 1))

    return (round(D,3))


def insereArestaLista(listaAdj, vi, vj):
    tipo = '0'

    # Verificando se é um grafo simples ou direcionado
    listas = listaAdj.keys()
    for v in listas:
        outros = listaAdj[v]
        for outro in outros:
            if v not in listaAdj[outro]:
                tipo = '1'
                break

    if tipo == '0':
            listaAdj[vi].append(vj)
            listaAdj[vi].sort()
            listaAdj[vj].insert(0, vi)
            listaAdj[vj].sort()

    else:
        listaAdj[vi].append(vj)
        listaAdj[vi].sort()

    return listaAdj


def insereVerticeLista(listaAdj):
    V = len(listaAdj)

    listaAdj[V] = []

    return listaAdj


def removeArestaLista(listaAdj, vi, vj):
    tipo = '0'

    # Verificando se é um grafo simples ou direcionado
    listas = listaAdj.keys()
    for v in listas:
        outros = listaAdj[v]
        for outro in outros:
            if v not in listaAdj[outro]:
                tipo = '1'
                break

    if tipo == '0':
        listaAdj[vi].remove(vj)
        listaAdj[vj].remove(vi)

    else:
        listaAdj[vi].remove(vj)

    return listaAdj


def removeVerticeLista(listaAdj, vi):
    listaAdj2 = {}

    for i in listaAdj:
        if i != vi:
            v = []
            for j in listaAdj[i]:
                if j != vi:
                    v.append(j)

            listaAdj2[i] = v

    return listaAdj2


def verificaAdjacenciaLista(listaAdj, vi, vj):

    if vj in listaAdj[vi]:
        return True
    else:
        return False


def warshall(matriz): # Usando pseudocódigo disponibilizado na matéria
    n = np.shape(matriz)[0]
    R = np.copy(matriz)

    for k in range(0,n):
        for i in range(0,n):
            for j in range (0,n):
                if (R[i][j] == 1) or (R[i][k] == 1) and (R[k][j] == 1):
                    R[i][j] = 1
                else:
                    R[i][j] = R[i][j]

    return R


def caminhoEuleriano(matriz): # Usando pseudocódigo disponibilizado na matéria
    matriz = np.array(matriz)
    n = np.shape(matriz)
    total = 0
    i = 0
    while (total <= 2) and (i < n[0]):
        grau = np.sum(matriz[i,:])
        if grau % 2 == 1:
            total += 1
        i += 1
    if total > 2:
        return (False)
    else:
        return (True)


def BFS(listaAdj, num):
    seq = []
    passou = {}

    for v in listaAdj:
        passou[v] = False

    lista = []

    while True:
        v1 = None
        for v in listaAdj:
            if not passou[v]:
                v1 = v
                break

        if v1 is None:
            break

        passou[v1] = True
        lista.append(v1)

        while lista:
            vAtual = lista.pop(0)
            seq.append(vAtual)

            if vAtual == num:
                if seq[0] == 0:
                    seq.pop(0)

            adjs = listaAdj[vAtual]

            for adj in adjs:
                if not passou[adj]:
                    passou[adj] = True
                    lista.append(adj)

    seq.insert(0, num)  # Insere o número inicial no resultado
    print(seq)


def DFSn(listaAdj, num, visitados=None):
    if visitados is None:
        visitados = [num]
    else:
        visitados.append(num)

    for adj in listaAdj[num]:
        if adj not in visitados:
            DFSn(listaAdj, adj, visitados)

    if num == visitados[0]:
        print(visitados)


def DFS(listaAdj, num):
    visitados = []
    p = [num]
    volta = False

    while p:
        v = p[-1]

        if v not in visitados:
            visitados.append(v)

        vizinhos = listaAdj[v]

        nVisitado = [vizinho for vizinho in vizinhos if vizinho not in visitados]

        if nVisitado:
            proxV = nVisitado[0]
            p.append(proxV)
            volta = False
        else:
            p.pop()
            volta = True

    res = [ver for ver in listaAdj.keys() if ver not in visitados]
    visitados.extend(res)

    print (visitados)


def ordenacaoTopologica(listaAdj):
    L = {}
    cor = {}
    tipoAresta = {}
    tempoD = {}
    tempoT = {}
    tempo = 0

    def visitaDFS(v):
        nonlocal tempo
        cor[v] = 'cinza'
        tempo += 1
        tempoD[v] = tempo

        for vertice in listaAdj[v]:
            if cor.get(vertice) == 'branco':
                tipoAresta[(v, vertice)] = 'Tree'
                visitaDFS(vertice)
            elif cor.get(vertice) == 'cinza':
                tipoAresta[(v, vertice)] = 'Back'
            else:
                if tempoD[v] < tempoD[vertice]:
                    tipoAresta[(v, vertice)] = 'Forward'
                else:
                    tipoAresta[(v, vertice)] = 'Cross'

        cor[v] = 'preto'
        tempo += 1
        tempoT[v] = tempo
        L[v] = tempo

    for v in listaAdj:
        cor[v] = 'branco'
        tempoT[v] = 0

    for v in listaAdj:
        if cor[v] == 'branco':
            visitaDFS(v)

    return list(sorted(L, key=L.get, reverse=True))



def classificaArestas(listaAdj, v):
    cor = {}
    tipoAresta = {}
    tempoD = {}
    tempoT = {}
    tempo = 0

    for ver in listaAdj.keys():
        cor[ver] = 'branco'
        tempoD[ver] = 'oi'
        tempoT[ver] = 'oi'

    def visitaDFS(v):
        nonlocal tempo
        cor[v] = 'cinza'
        tempo += 1
        tempoD[v] = tempo

        for vertice in listaAdj[v]:
            if cor[vertice] == 'branco':
                tipoAresta[(v, vertice)] = 'Tree'
                visitaDFS(vertice)
            elif cor[vertice] == 'cinza':
                tipoAresta[(v, vertice)] = 'Back'
            else:
                if tempoD[v] < tempoD[vertice]:
                    tipoAresta[(v, vertice)] = 'Forward'
                else:
                    tipoAresta[(v, vertice)] = 'Cross'

        cor[v] = 'preto'
        tempo += 1
        tempoT[v] = tempo

    for v in listaAdj.keys():
        if cor[v] == 'branco':
            visitaDFS(v)

    res = ''
    for (v, vertice) in tipoAresta.keys():
        res += str(v) + ' ' + str(vertice) + ' ' + tipoAresta[(v, vertice)] + '\n'

    return res


def temposVertices(listaAdj, v):
    tempoD = {}
    tempoT = {}
    t = 0
    def visitaDFS(ver, t):
        t += 1
        tempoD[ver] = t

        for adj in listaAdj[ver]:
            if adj not in tempoD:
                t = visitaDFS(adj, t)

        t += 1
        tempoT[ver] = t
        return t

    t = visitaDFS(v, t)

    for ver in listaAdj:
        if ver not in tempoD:
            t = visitaDFS(ver, t)

    resFinal = {}
    for ver in listaAdj:
        if ver in tempoD:
            resFinal[ver] = "{}/{}".format(tempoD[ver], tempoT[ver])

    return resFinal

def verificaDAG(listaAdj):
    L = []
    S = []
    E = []

    # Inicializa os vértices sem arcos de entrada
    for v in listaAdj:
        if not any(v in adj for adj in listaAdj.values()):
            S.append(v)

    # Constrói a lista de arestas
    for v in listaAdj:
        for w in listaAdj[v]:
            E.append((v, w))

    while S:
        v = S.pop(0)
        L.append(v)

        # Remove o arco (v, w) de E e atualiza S
        for arc in list(E):
            if arc[0] == v:
                w = arc[1]
                E.remove(arc)
                if not any(w == adj[1] for adj in E):
                    S.append(w)

    if E:
        return "NÃO DAG"
    else:
        return "DAG"

import numpy as np

def dijkstra(matriz, vOrigem, vDestino):
    num_vertices = len(matriz)

    # Inicialização dos custos e rotas
    custo = np.full(num_vertices, float('inf'), dtype=float)
    rota = np.zeros(num_vertices, dtype=int)
    custo[vOrigem] = 0

    A = set(range(num_vertices))
    F = set()

    while A:
        v = min(A, key=lambda x: custo[x])  # Vértice em A com menor custo[v]
        F.add(v)
        A.remove(v)

        for u in range(num_vertices):
            if u not in F:
                if matriz[v][u] != -1:  # Verifica se há uma conexão entre v e u
                    if custo[v] + matriz[v][u] < custo[u]:
                        custo[u] = custo[v] + matriz[v][u]
                        rota[u] = v

    caminho = []
    v = vDestino
    while v != vOrigem:
        caminho.append(v)
        v = rota[v]
    caminho.append(vOrigem)
    caminho.reverse()

    custo_minimo = int(custo[vDestino])

    return (caminho, custo_minimo)


import numpy as np

def bellmanFord(matriz, vOrigem, vDestino):
    matriz = np.array(matriz)
    V = matriz.shape[0]
    custo = [float('inf')] * V
    rota = [-1] * V

    custo[vOrigem] = 0

    for i in range(V - 1):
        for v in range(V):
            for u in range(V):
                if matriz[v, u] != -1:  # Verifica se a aresta existe (valor diferente de -1)
                    if custo[u] > custo[v] + matriz[v, u]:
                        custo[u] = custo[v] + matriz[v, u]
                        rota[u] = v

    for v in range(V):
        for u in range(V):
            if matriz[v, u] != -1:  # Verifica se a aresta existe (valor diferente de -1)
                if custo[u] > custo[v] + matriz[v, u]:
                    return False

    caminho = [vDestino]
    custo_caminho = custo[vDestino]

    while vDestino != vOrigem:
        vDestino = rota[vDestino]
        caminho.insert(0, vDestino)

    return (caminho, custo_caminho)


def floydWarshall(matriz):
    n = len(matriz)
    D = np.copy(matriz)

    for k in range(n):
        for v in range(n):
            for u in range(n):
                if D[v][k] != -1 and D[k][u] != -1:
                    if D[v][u] == -1 or D[v][u] > D[v][k] + D[k][u]:
                        D[v][u] = D[v][k] + D[k][u]

    return D
















