import sys
from Inicializacao import (dataSet as ds, grafo as g)

def main(instancia):

    # instanciaEscolhida retorna o grafo lido em uma matriz do tipo Numpy
    instanciaEscolhida = g.lerGrafo(instancia)
    vi = 0
    vj = 2
    adjacencia = g.verificaAdjacencia(instanciaEscolhida, vi, vj)
    print(adjacencia)
    # matriz retorna o valor da quantidade de linhas e colunas da matriz instanciaEscolhida
    matriz = ds.qtdShape(instanciaEscolhida)
    lista = g.criaListaAdjacencias(instanciaEscolhida)
    tipoLista = g.tipoGrafoLista(lista)
    densidadeLista = g.calcDensidadeLista(lista)
    insereAresta = g.insereArestaLista(lista, vi, vj)

    # Prints dos resultados obtidos, testando todas as funções para entrega separada
    print(str(instancia))
    print(matriz)
    print(instanciaEscolhida)
    print(lista)
    print(tipoLista)
    print(densidadeLista)
    print(insereAresta)

    # Para salvar em arquivo
    resultado = [str(instancia), matriz, instanciaEscolhida] # Lista de tipo misto com valores dos resultados
    ds.salvaResultado(resultado) # Salva resultado em arquivo

'''Chamada a função main()
   Argumento Entrada: [1] dataset'''
if __name__ == '__main__':
    main(str(sys.argv[1]))

