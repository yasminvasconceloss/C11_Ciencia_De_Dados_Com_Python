#Questão 5
#Encontre qual país da América do Sul e Caribe (LATIN AMER. & CARIB) possui
#a maior renda per capita (GDP ($ per capita));

import numpy as np
dataset = np.loadtxt('paises.csv', delimiter=';', dtype=str, encoding='utf-8') #dtype=str -> traz tudo em formato de texto
print(dataset)
print("")

dados = dataset[1:]

paises = dados[:, 0]
regioes = dados[:, 1]
rendaPerCapita = dados[:, 8].astype(int)

Caribe = np.char.startswith(regioes, 'LATIN AMER. & CARIB')

rendaPerCapitaCaribe = rendaPerCapita[Caribe]
paisesCaribe = paises[Caribe]
indice_max = np.argmax(rendaPerCapitaCaribe)

print("País com a maior renda per capita: ", paisesCaribe[indice_max], ". Valor da renda: ", rendaPerCapitaCaribe[indice_max])