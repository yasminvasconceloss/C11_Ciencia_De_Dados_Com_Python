#Questão 3
#Mostre qual a taxa média de alfabetização (Literacy (%)) do planeta segundo este dataset;

import numpy as np
dataset = np.loadtxt('paises.csv', delimiter=';', dtype=str, encoding='utf-8') #dtype=str -> traz tudo em formato de texto
print(dataset)
print("")

dados = dataset[1:]
literacy = dados[:, 9].astype(float)
print("A taxa média de alfabetização é: ", np.mean(literacy))