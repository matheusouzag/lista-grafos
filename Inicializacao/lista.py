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