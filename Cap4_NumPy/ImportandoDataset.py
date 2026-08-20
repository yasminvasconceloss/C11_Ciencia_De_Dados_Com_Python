import numpy as np
dataset = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8') #dtype=str -> traz tudo em formato de texto
print(dataset)

#delimiter=';' → separa as colunas pelo ;
#dtype=str → transforma tudo em texto
#encoding='utf-8' → informa a codificação do arquivo

#Extraindo as colunas do dataset
print(dataset[0,:])

#Extraindo o nome das empresas
print(dataset[1:, 1])

#Removendo resultados repetidos
print(np.unique(dataset[1:, 1], return_counts=True))


