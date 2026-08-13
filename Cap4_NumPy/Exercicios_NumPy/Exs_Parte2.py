"""4. Crie uma matriz de tamanho qualquer. Extraia seu número de linhas
e colunas, multiplique-os, e diga se esta matriz poderia se tornar um vetor
unidimensional com número par ou ímpar de elementos"""

import numpy as np

mtz = np.array([ [2, 4, 6], [8, 10, 12], [14, 16, 18]]) #3x3
print(mtz)

linha, coluna = mtz.shape #retornando tupla com o tamanho da matriz
print(f'Número de linhas e colunas: {mtz.shape}')

total = linha * coluna
print(f'Multiplicação de linhas e colunas: {total}')

if total % 2 == 0:  #par
    print('A matriz pode se tornar um vetor unidimensional com número PAR de elementos')
else:
    print('A matriz pode se tornar um vetor unidimensional com número ÍMPAR de elementos')

vetor = mtz.reshape(-1)
print(vetor)





'''5. Crie uma matriz de tamanho 4x4 formada por números aleatórios inteiros entre 1 e 50 (use seed = 10 antes)
    a) Mostre o resultado da média de cada linha e cada coluna da matriz gerada
    b) Apresente o maior valor das médias das linhas e também das colunas
    c) Mostre a quantidade de aparições de cada um dos números gerados na
    matriz. Em seguida, mostre apenas os números que aparecem 2 vezes '''

import numpy as np

np.random.seed(10) #começando sequencia de aleatórios a partir do 10

mtz = np.random.randint(2, 50, size=(4, 4))
print(mtz)
print("")

soma_linha = mtz.sum(axis = 1)
print(soma_linha)

soma_coluna = mtz.sum(axis = 0)
print(soma_coluna)

print('')

# Media
media_linha = soma_linha/4
print(f'Média da linha: {media_linha}')

media_coluna = soma_coluna/4
print(f'Média da coluna: {media_coluna}')

print('')

#Maior Média
maior_media_linha = media_linha.max()
print(f'Maior média da Linhas: {maior_media_linha}')

maior_media_coluna = media_coluna.max()
print(f'Maior média da Coluna: {maior_media_coluna}')

print('')

#Número de aparições e as que aparecem duas vezes
print(np.unique(mtz))
print(np.unique(mtz, return_counts=True))