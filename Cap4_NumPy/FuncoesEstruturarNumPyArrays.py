#FUNCOES PARA ESTRUTURARMOS NUMPY ARRAYS
import numpy as np

#ones
mtz = np.ones([5,5])
print(mtz)

#zeros
arr = np.zeros(10)
print(arr)
print(arr.reshape(5,2)) #reshape = transformar arrays unidimensionais em bidimensionais

#Arange
mtz = np.arange(2,21,2) #de 2 a 20
print(mtz)
print(mtz.reshape(2,5))


#OPERACOES ENTRE NUMPY ARRAYS
arr1 = np.array([10,20,30,40,50])
arr2 = np.array([60,40,20,10,5])
arr3 = arr1 + arr2

print(arr3)
print(arr1-arr2)
print(arr1*arr2)

#CONCATENAÇÃO DE ARRAYS
arr3 = np.concatenate([arr1,arr2])
print(arr3)

#Broadcasting - quando um ESCALAR faz uma operação com um ARRAY
print(5*arr3)

#ESTRUTURANDO UMA MATRIZ COM CONTAS
mtz = np.arange(10, 96, 5) # de 10 a 95 em intervalos de 5
print(mtz.size)
mtz = mtz.reshape(3, 6)
print(mtz)

#EXTRAINDO A SOMA DA PRIMEIRA COLUNA (NET)
print(mtz.sum(axis=0)) #Eixo 0=coluna. Axis -> somar valor das colunas
print(mtz.sum(axis=0)[0]) #slicing -> valor so da soma da primeira coluna, sem o colchete soma tudo

#EXTRAINDO A SOMA DA SEGUNDA LINHA (FEV)
print(mtz.sum(axis=1)) #Eixo 0=coluna. Axis -> somar valor das colunas
print(mtz.sum(axis=1)[1]) #slicing -> valor so da soma da primeira coluna, segunda linha

#NUMEROS ALEATORIOS NO NUMPY (Módulo Random)
rand = np.random.randint(10)
rand1 = np.random.randint(5, 10) #delimitando
print(rand)
print(rand1)
rand2 = np.random.randint(1, 10, 10) #matriz random
print(rand2)

#PLANTANDO A SEMENTE ALEATORIA
np.random.seed(5)
array = np.random.randint(1,10,10)
print(array)

#EXTRAINDO ELEMENTOS ÚNICOS
print(np.unique(array))

#CONTANDO ELEMENTOS UNICOS
print(np.unique(array, return_counts=True))