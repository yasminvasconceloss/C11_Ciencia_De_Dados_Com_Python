#Questão 2
#Conte e em seguida mostre quais são as diferentes Regiões do planeta segundo este dataset;

import numpy as np
dataset = np.loadtxt('paises.csv', delimiter=';', dtype=str, encoding='utf-8') #dtype=str -> traz tudo em formato de texto
print(dataset)
print("")

dados = dataset[1:]
regioes = dados[:, 1]
regioesDiferentes = np.unique(regioes)
contagemRegioes = len(regioesDiferentes)

print("Quantidade de regiões diferentes: ", len(regioesDiferentes))
print(regioesDiferentes)