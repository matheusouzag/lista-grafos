import sys
from Inicializacao import (lista as lis, matriz as ma)

def main(instancia):

    # instanciaEscolhida retorna o grafo lido em uma matriz do tipo Numpy
    instanciaEscolhida = ma.lerGrafo(instancia)
    vi = 0
    vj = 3
    adjacencia = ma.verificaAdjacencia(instanciaEscolhida, vi, vj)
    print(adjacencia)
    # matriz retorna o valor da quantidade de linhas e colunas da matriz instanciaEscolhida
    matriz = lis.qtdShape(instanciaEscolhida)
    lista = lis.criaListaAdjacencias(instanciaEscolhida)
    tipoLista = lis.tipoGrafoLista(lista)
    densidadeLista = lis.calcDensidadeLista(lista)
    #insereAresta = lis.insereArestaLista(lista, vi, vj)
    #insereVertice = lis.insereVerticeLista(lista)
    #removeArestaLista = lis.removeArestaLista(lista, vi, vj)
    #removeVerticeLista = lis.removeVerticeLista(lista,vi)
    verificaAdj = lis.verificaAdjacenciaLista(lista, vi, vj)

    # Prints dos resultados obtidos, testando todas as funções para entrega separada
    print(str(instancia))
    print(matriz)
    print(instanciaEscolhida)
    print(lista)
    print(tipoLista)
    print(densidadeLista)
    #print(insereAresta)
    #print(removeArestaLista)
    #print(removeVerticeLista)
    print(verificaAdj)

    # Para salvar em arquivo
    resultado = [str(instancia), matriz, instanciaEscolhida] # Lista de tipo misto com valores dos resultados
    lis.salvaResultado(resultado) # Salva resultado em arquivo

'''Chamada a função main()
   Argumento Entrada: [1] dataset'''
if __name__ == '__main__':
    main(str(sys.argv[1]))

