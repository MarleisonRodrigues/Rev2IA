#Dada o quebra-cabeça de 8 peças. Faça um programa que receba um estado do jogo e retorne
#todos estados subsequentes possíveis.

#Passo 1: ler uma matriz 3x3
#Passo 2: depois encontrar a posição vazia
#Passo 3: Gerar os estados subsequentes, (mantem linha soma e diminui coluna, e vice-versa, lembrando dos indices menores e iguais a zero)


import random #biblioteca para gerar numeros aleatorios
import copy   #biblioteca para fazer copia das estruturas de dados



META = [[1,2,3], [4,5,6],[7,8,0]]

#classe Nó em que cada nó vai quardar o endereço do nó pai para realizar a busca
class Noh:
    def __init__(self, estado, nopai, g, h): #função inicial
        self.estado = estado
        self.pai = nopai
        self.g = g
        self.h = h

    def __eq__(self, outro): #função para verificar se um nó é igual ao outro
        return self.estado == outro.estado

    def __repr__(self): #função para imprimir o valor de um nó
        return str(self.estado)

    def getState(self): #função para retornar o estado do nó
        return self.estado

#Passo 1:
#Função para gerar o tabuleiro inicial
def geraInicial(st=META[:]):
    lista = [j for i in st for j in i]
    while True:
        random.shuffle(lista)
        st = [lista[:3]]+[lista[3:6]]+[lista[6:]]

#Passo 2:
#Funcao que vai localizar um elemento qualquer no tabuleiro, por padrao encontrará o espaço em branco
def localizar(estado,elemento=0):
    for i in range(3):
        for j in range(3):
            if estado[i][j]==elemento:
                linha = i
                coluna = j
                return linha,coluna
#Dado dois estado quaisquer, Localizará a distancia quateirao total dos estados 
def distanciaQuarteirao(st1,st2):
    dist = 0
    fora = 0
    for i in range(3):
        for j in range(3):
            if st1[i][j]==0: continue
            i2,j2 = localizar(st2,st1[i][j])
            if i2 != i or j2 != j: fora += 1
            dist += abs(i2-i)+abs(j2-j)
    return dist + fora
def criaNo(estado,pai,g=0):
    h = g + distanciaQuarteirao(estado,META) #heuristica A*
    return Noh(estado,pai,g,h)

#funçao para inserir nó na variavel de controle da busca
def inserirNoh(noh,fronteira):
    if noh in fronteira:
        return fronteira
    fronteira.append(noh)
    chave = fronteira[-1]
    j = len(fronteira)-2
    while fronteira[j+1].h > chave.h and j>=0:
        fronteira[j+1] = fronteira[j]
        fronteira[j] = chave
        j-=1
    return fronteira


#Passo 3:
#retornar todos os sucessores de um nó
def succ(noh):
    estado = noh.estado
    pai = noh.pai 
    if pai:
        estadoPai = pai.estado
    else:
        estadoPai = None
    listaS = []
    l1 = moverAcima(copy.deepcopy(estado))
    if l1 != estado:
        listaS.append(l1)
    l2 = moverDireita(copy.deepcopy(estado))
    if l2 != estado:
        listaS.append(l2)
    l3 = moverAbaixo(copy.deepcopy(estado))
    if l3 != estado:
        listaS.append(l3)
    l4 = moverEsquerda(copy.deepcopy(estado))
    if l4 != estado:
        listaS.append(l4)
    return listaS

#Passo 3: continuação   
#Função dos movimentos do tabuleiro, ou seja, movendo o espaço
def moverAbaixo(estado):
    linha,coluna = localizar(estado)
    if linha < 2:
        estado[linha+1][coluna],estado[linha][coluna] = estado[linha][coluna],estado[linha+1][coluna]
    return estado

def moverAcima(estado):
    linha,coluna = localizar(estado)
    if linha > 0:
        estado[linha-1][coluna],estado[linha][coluna] = estado[linha][coluna],estado[linha-1][coluna]
    return estado

def moverDireita(estado):
    linha,coluna = localizar(estado)
    if linha < 2:
        estado[linha][coluna+1],estado[linha][coluna] = estado[linha][coluna],estado[linha][coluna+1]
    return estado

def moverEsquerda(estado):
    linha,coluna = localizar(estado)
    if linha > 0:
        estado[linha][coluna-1],estado[linha][coluna] = estado[linha][coluna],estado[linha][coluna-1]
    return estado


#função de busca  A*
def busca(max,nohInicio):
    print(nohInicio,":")
    nmov = 0
    borda = [nohInicio]
    while borda:
        noh = borda.pop(0)
        if noh.estado == META:
            sol = []
            while True:
                sol.append(noh.estado)
                noh = noh.pai
                if not noh: break
            sol.reverse()
            return sol,nmov
        nmov+=1
        if (nmov%(max/10))==0: print(nmov, end="....")
        if nmov>max: break
        sucs = succ(noh)
        for s in sucs:
            inserirNoh(criaNo(s,noh,noh.g+1),borda)
    return 0,nmov

def imprime_as_jogadas(tab):
    print("\nAs jogadas foram:")
    lista = []
    while (tab[3][1] != None):  # vai até o nó raiz
        lista.append(tab)
        tab = tab[3][1]
    lista.append(tab)
    while (len(lista) > 0):
        temp = lista.pop()
        imprime_tabuleiro(temp)

#main


noInicial = criaNo(geraInicial(), None)
res,nmov = busca(max, noInicial)
imprime_as_jogadas(max)


#código dificil para fazer, tentando entender python agora então a colcha de retalho ta bugada ainda :(