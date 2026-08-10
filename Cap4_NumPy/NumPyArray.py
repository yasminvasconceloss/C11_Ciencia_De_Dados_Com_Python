import numpy as np

#CRIANDO UM NUMPY ARRAY 1D
arr = np.array([10,20,30,40,50,60])
print(arr)
print(type(arr))

#PROPRIEDADES DO ARRAY
print(arr.size)
print(arr.ndim)
print(arr.shape)

mtz = np.array([[10,20], [30,40], [50,60]])
print(mtz)

#PROPRIEDADES DO ARRAY
print(mtz.size)
print(mtz.ndim)
print(mtz.shape) # formato => linhas por colunas

