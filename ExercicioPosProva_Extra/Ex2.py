# Para esta questão, faça o que se pede em ordem:
# a. Crie dois NumPy Arrays 1-D com 4 nomes de pessoas cada;
# b. Em seguida, concatene-os em um só Array;
# c. Transforme o Array final em um Array 2-D com mais colunas do que linhas;
# d. Por fim, ordene os nomes do Array 2-D em ordem decrescente.

import numpy as np

# Criando dois Arrays 1-D com 4 nomes cada
nomes1 = np.array(['Ana', 'Carlos', 'João', 'Mariana'])
nomes2 = np.array(['Pedro', 'Beatriz', 'Lucas', 'Fernanda'])

print('Array 1:', nomes1)
print('Array 2:', nomes2)

# Concatenando os dois Arrays em um só
nomes = np.concatenate((nomes1, nomes2))

print('\nArray concatenado:', nomes)

# Transformando o Array final em um Array 2-D -> São 8 nomes,  2 linhas e 4 colunas
nomes2D = nomes.reshape(2, 4)

print('\nArray 2-D:')
print(nomes2D)

# Ordenando os nomes em ordem decrescente
nomesOrdenados = np.sort(nomes2D)
nomesOrdenados = nomesOrdenados[:, ::-1]

print('\nNomes em ordem decrescente:')
print(nomesOrdenados)