# Usando recursividade, faça um programa que calcule a soma dos valores de um vetor.


tamvetor = int(input('Digite o tamanho do vetor:'))

#inserindo valores no vetor e imprimindo esse vetor
vetor=[]
for i in range (0,tamvetor): 
    vetor.append(int(input('Digite um número:')))
print(vetor)

#Função recursiva para realizar a soma dos valores do vetor e retornar o valor da soma
def soma_vetor(vetor):
    if len(vetor) == 1:
        return vetor[0]
    else:
        return vetor[0] + soma_vetor(vetor[1:])
 
print("A soma do vetor é: ", soma_vetor(vetor))
