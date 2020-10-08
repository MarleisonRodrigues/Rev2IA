# Faça um programa que leia 10 tarefas. Cada tarefa contém uma descrição (string) e a ordem que
#ela deve ser executada (utilizar classe ou estrutura para representar a tarefa). As tarefas devem ser
#inseridas em um vetor. O programa deve imprimir a descrição tarefas em ordem de execução

import heapq

#Classe para representar as tarefas pegando sua descrição e prioridade
class Tarefas: 
    def init (self, desc, prio):
        self.desc=desc
        self.prior=prio
    def setDesc(self,desc): 
        self.desc=desc
    def getDesc(self):
        return self.desc
    def setPrio(self, prio):
        self.prio=prio
    def getPrio(self):
       return self.prior

#Criando uma lista e armazenando os valores, 10 tarefa e sua ordem de execução
# aqui vamos colocar 2 valores para ficar facil o teste, onde for dois so trocar por 10
lista=[]
for i in range (0,2):
    tarefa=input('Digite a tarefa {} : '.format(i+1))
    ordem =int(input('Digite sua ordem de execução da tarefa {} : '.format(i+1)))
    while ordem>2 or ordem<0:
        ordem =int(input('INVALIDO, digite a ordem de execução da tarefa {} : '.format(i+1)))
    t=(tarefa,ordem)

# Remover e devolver o primeiro elemento do heap.
    heapq.heappush(lista,(ordem, tarefa))

#Imprimir as tarefas da lista em ordem de execução
for i in range (0,2):
    print(lista[-i][1])
    heapq.heappop(lista)
   
