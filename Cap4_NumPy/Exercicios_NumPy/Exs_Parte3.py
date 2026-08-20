import numpy as np
dataset = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8') #dtype=str -> traz tudo em formato de texto
print(dataset)
print("")

#1. Apresente a porcentagem de missões que deram certo

statusMissoes = dataset[1:, 7] # 1: Começando da linha de indice 1 até o final | 7 = considerando apenas a coluna de índice 7
qtdSucesso = np.sum(statusMissoes == 'Success')
porcentagem = (qtdSucesso / len(statusMissoes)) * 100 # len(status_missões) -> contando a qtd total das missoes
print(f"Porcentagem de missões com sucesso: {porcentagem:.2f}%")
print("")

#2. Qual a media de gastos de uma missão especial se baseando em missões que possuam valores disponíveis (>0)?

colunaGastos = dataset[1:, 6].astype(float)
gastosValidos = colunaGastos[colunaGastos > 0] # Armazenando apenas custos >0
somaGastos = np.sum(gastosValidos)
mediaGastos = somaGastos / len(gastosValidos)
print(f'Média de gastos de missões espaciais: {mediaGastos:.2f}')
print('')

#3. Encontre quantas missões espaciais neste Dataset foram realizadas pelos Estados Unidos (EUA)

locais = dataset[1:, 2]
missoesEUA = np.char.find(locais, 'USA') != -1 # Mostrando o array das posições do EUA | != -1 = Removendo as posições restantes
qtd = np.sum(missoesEUA)
print(f'Quantidade de missões espaciais feitas pelos EUA: {qtd}')
print('')

#4. Encontre qual foi a missão mais cara realizada pela empresas “SpaceX”

empresas = dataset[1:, 1]
nomesMissoes = dataset[1:, 4]
custos = dataset[1:, 6].astype(float)

Spacex = empresas == 'SpaceX'
custosSpacex = custos[Spacex]
missoesSpacex = nomesMissoes[Spacex]

maiorCusto = np.argmax(custosSpacex)
missaoMaisCara = missoesSpacex[maiorCusto]
print(f"A missão mais cara da SpaceX foi: {missaoMaisCara}")
print("")

#5. Mostre o nome das empresas que já realizaram missões espaciais, juntamente
# com suas respectivas quantidades de missões (use o for no final para mostrar as informações)

empresas, qtd = np.unique(empresas, return_counts=True)

for nome, qtd in zip(empresas, qtd):
    if qtd == 1:
        print(f"{nome}: {qtd} missão")
    else:
        print(f"{nome}: {qtd} missões)")