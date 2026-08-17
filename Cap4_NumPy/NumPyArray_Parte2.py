import numpy as np

#---------SLICING NO NUMPY----------

#Plantando a mesma semente aleatória(numeros aleatorios iguais independente da máquina)
np.random.seed(10)

mtz = np.random.randint(1, 99, 9).reshape(3,3) #gerar números aleatórios (entre 1 e 99, gerar 9 valores) -> transformar em matriz usando reshape
print(mtz)

#Extraindo apenas a segunda linha da matriz
print(mtz[1])

#Extraindo apenas a terceira coluna da matriz
print(mtz[:,2])

#Extraindo a matriz 2x2 no canto inferior direito da matriz original
print(mtz[1:,1:])



#---------CONDICIONAIS NO NUMPY----------
print(mtz)

#Mostrando apenas os elementos menores que 70
print(mtz<70)
print(mtz[mtz<70])

#Retorne apenas os números pares
print(mtz%2==0)
print(mtz[mtz%2==0])


#---------ANÁLISE DE PADRÕES TEXTUAIS COM NUMPY----------
arr = np.array(['Inatel', 'Casa Viva',
                'ICC', 'CDG', 'eHealth',
                'CSILab', 'RobotBulls',
                'ProdLab', 'CRA', 'CRR'])

print(arr)

#Submodulo do NumPy para trabalhar com texto: char
#Buscando qual texto aceita um padrão informado

print(np.char.find(arr, 'A')) #palavras que tem A
print(np.char.find(arr, 'A')>=0)
cond = np.char.find(arr, 'A')>=0
print(arr[cond])


#transformando tudo em maiúsculo para captar A e a
arr = np.char.upper(arr)
print(np.char.find(arr, 'A')) #palavras que tem A
print(np.char.find(arr, 'A')>=0)
cond = np.char.find(arr, 'A')>=0
print(arr[cond])

