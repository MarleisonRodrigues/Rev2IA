#Dado o grafo representado na imagem a seguir. Faça um programa que leia um arquivo contendo
#informações do grafo, gere uma matriz de adjacência e calcule o grau de cada vértice.
import copy     

vert = []
arest = []
mat = []

class Aresta:
    def __init__(self, n1, n2, peso):
        self.n1 = n1
        self.n2 = n2
        self.peso = peso

arquivo = open('grafo6.txt', 'r')
for i in arquivo:
    grafo = i.split()
    arest.append(Aresta(int(grafo[0]), int(grafo[1]), int(grafo[2])))
arquivo.close() 

def inserido(vertice):
    inserted = False
    for i in range( len(vert) ):
        if (vertice == vert[i]):
            inserted = True
            break
    return inserted

#Iterar para preencher a lista 'vertices'
for i in range( len(arest) ):
    if(not inserido(arest[i].n1)):
        vert.append(arest[i].n1)
    if(not inserido(arest[i].n2)):
        vert.append(arest[i].n2)
vert = sorted(vert)

#Preencher matriz com zeros
for i in range( len(vert) ):
    grafo = []
    for j in range( len(vert) ):
        grafo.append(0)
    mat.append(grafo)

#Criando matriz adjacente
for i in range( len(arest) ):
    mat[arest[i].n1][arest[i].n2] = arest[i].peso
    mat[arest[i].n2][arest[i].n1] = arest[i].peso
    
#Imprimir Matriz
print()
print("A Matriz de Adjacencia é: ")
for i in range( len(mat) ):
    print(mat[i])
print()

#Calculando e imprimindo o grau de cada vértice:
print("O grau de cada vértice é: ")
for i in range( len(mat) ):
    grau = 0
    for j in range( len(mat[i]) ):
        if(mat[i][j] != 0):
            grau += 1
    print('Grau de {}: {}'.format(i,grau) )


# Busca em Profundidade
'''def dfs(grafo):
    def dfs_recursiva(grafo, vert):
        visitados.add(vert)
        for vizinho in grafo[vert]:
            if vizinho not in visitados:
                dfs_recursiva(grafo, vizinho)

    visitados = set()
    for vert in grafo:
        if not vert in visitados:
            dfs_recursiva(grafo, vert)'''

def dfs(grafo, vert):
    visitados = set()

    def dfs_iterativa(grafo, vert):
        visitados.add(vert)
        falta_visitar = [vert]
        while falta_visitar:
            vert = falta_visitar.pop()
            for vizinho in grafo[vert]:
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    falta_visitar.append(vizinho)

    dfs_iterativa(grafo, vert)

#dfs(grafo, 0)

