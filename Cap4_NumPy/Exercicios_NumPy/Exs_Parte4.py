import numpy as np
dataset = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8') #dtype=str -> traz tudo em formato de texto
print(dataset)
print("")

#6. Qual a porcentagem de missões realizadas com foguetes cujo status é "StatusRetired" (coluna Status Rocket)?

colunaStatusRocket = dataset[1:, 5] # Pegando coluna Status Rocket

qtd = np.sum(colunaStatusRocket == 'StatusRetired')
porcentagemStatusRetired = (qtd / len(colunaStatusRocket)) * 100
print(f'A porcentagem de missões com foguetes cujo status é StatusRetired é: {porcentagemStatusRetired:.2f}')
print("")

#7. Quantas missões foram lançadas a partir de localizações que contêm "Russia" (coluna Location)?

colunaLocation = dataset[1:, 2]

missoesRussia = np.char.find(colunaLocation, 'Russia')!= -1
qtdMissoesRussia = np.sum(missoesRussia)
print(f'A quantidade de missões lançadas pela Rússia foi: {qtdMissoesRussia}')
print("")

#8. Encontre a empresa e o valor da missão mais cara de todo o Dataset.

empresas = dataset[1:, 1]
valor = dataset[1:, 6].astype(float)

MaisCaro  = valor[0]
indiceMaiorCusto = 0

for i in range(len(valor)):
    if valor[i] > MaisCaro:
        MaisCaro = valor[i]
        indiceMaiorCusto = i

empresaMaisCara = empresas[indiceMaiorCusto]
print(f"A missão mais cara foi feita pela empresa: {empresaMaisCara}")
