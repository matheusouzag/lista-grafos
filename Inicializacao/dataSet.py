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