# Os valores de cores RGBA são uma extensão dos valores de cores RGB
# com um canal alfa que especifica a opacidade de uma cor. Baseado na coleção abaixo, faça:
# a. Mostre apenas o nome das cores que são primárias;
# b. Mostre apenas os códigos hexadecimais das cores que possuem tom de azul máximo (255);
# c. Crie um NumPy Array 1-D formado apenas pelo nome e código hexadecimal de cada cor;
# d. Transforme o Array 1-D em um Array 2-D com o nome e código;
# e. Troque o nome de cada cor no Array 2-D para seu respectivo nome em Português.

import numpy as np


colors = [
    {"color": "black", "type": "primary", "code": {"rgba": [255, 255, 255, 1], "hex": "#000"}},
    {"color": "green", "type": "secondary", "code": {"rgba": [0, 255, 0, 0.1], "hex": "#0F0"}},
    {"color": "yellow", "type": "primary", "code": {"rgba": [255, 255, 0, 0.7], "hex": "#FF0"}},
    {"color": "blue", "type": "primary", "code": {"rgba": [0, 0, 255, 1], "hex": "#00F"}}
]


#Mostrando apenas o nome das cores que são primárias

for cor in colors:
    if cor["type"] == "primary":
        print(cor["color"])


#Mostrando apenas os códigos hexadecimais das cores que possuem tom de azul máximo (255)

for cor in colors:
    if cor["code"]["rgba"][2] == 255:
        print(cor["code"]["hex"])


# c. Criando um NumPy Array 1-D apenas com o nome e o código hexadecimal de cada cor

array = []

for cor in colors:
    array.append(cor["color"])
    array.append(cor["code"]["hex"])

array = np.array(array)

print('\nArray 1-D:')
print(array)


# d. Transformando o Array 1-D em um Array 2-D com o nome e código hexadecimal

array2D = array.reshape(4, 2)

print('\nArray 2-D:')
print(array2D)

#Trocando o nome das cores para Português

array2D[0, 0] = 'preto'
array2D[1, 0] = 'verde'
array2D[2, 0] = 'amarelo'
array2D[3, 0] = 'azul'

print('\nArray 2-D com os nomes em Português:')
print(array2D)