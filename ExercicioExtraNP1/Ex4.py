#Questão 4
#Conte quantos países são da América do Norte (NORTHERN AMERICA) segundo este dataset;

import numpy as np
dataset = np.loadtxt('paises.csv', delimiter=';', dtype=str, encoding='utf-8') #dtype=str -> traz tudo em formato de texto
print(dataset)
print("")

dados = dataset[1:]
regioes = dados[:, 1]
qtd_america_norte = np.sum(np.char.startswith(regioes, 'NORTHERN AMERICA'))

print(qtd_america_norte)