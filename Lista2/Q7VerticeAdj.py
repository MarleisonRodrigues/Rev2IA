#Dado o grafo anterior, faça um programa que leia um vértice e retorne os vértices adjacentes a ele.

vert = []
arest = []
mat = []

class Aresta:
    def __init__(self, n1, n2, peso):
        self.n1 = n1
        self.n2 = n2
        self.peso = peso

#faz a leitura do arquivo 
arquivo = open('grafo6.txt', 'r')
for i in arquivo:
    linha = i.split()
    arest.append(Aresta(int(linha[0]), int(linha[1]), int(linha[2])))
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
    linha = []
    for j in range( len(vert) ):
        linha.append(0)
    mat.append(linha)

#Criando matriz adjacente
for i in range( len(arest) ):
    mat[arest[i].n1][arest[i].n2] = arest[i].peso
    mat[arest[i].n2][arest[i].n1] = arest[i].peso

try:
    v = int(input("Digite o vértice: "))
except ValueError as e:
    print("Erro: {}".format(e))
    exit()

exist = False
for i in range( len(vert)):
    if v == vert[i]:
        exist = True
        break
if exist == False:
    print("Não há este vértice no grafo")
    exit()

adjacentes = []
for i in range(len (mat[v]) ):
    if mat[v][i] != 0:
        adjacentes.append(i)
print("Os vertices adjacentes são: ")
print(adjacentes)