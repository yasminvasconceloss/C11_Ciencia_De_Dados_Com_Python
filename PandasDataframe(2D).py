import numpy as np
import pandas as pd

#Como preencher um Dataframe (como uma planilha)
#Lista de labels (colunas)

colunas = ['W', 'X', 'Y', 'Z']

#Lista de labels (Linhas)
linhas = ['A', 'B', 'C', 'D', 'E']

np.random.seed(10) #plantando a semente aleatória

#Lista de Valores
valores = np.random.randint(1, 50, [5, 4])

df = pd.DataFrame(columns=colunas,
                  index=linhas,
                  data=valores)

print(df)

#Puxando uma unica coluna do Dataframe
print (df['X'])

#Puxando duas colunas do Dataframe
print (df[['Y', 'Z']])

#Puxando uma única célula
print(df['Y']['C'])

#Puxando Multipas colunas
print(df[['W', 'X', 'Z']])

#SLICING DE DADOS NO DATAFRAME COM LOC (LABELS) E ILOC (INDICES NUMERICOS)

#PUXANDO UMA UNICA LINHA DO DATAFRAME
print(df.loc['C',['W', 'X', 'Y', 'Z']])
print(df.iloc[2, :])

#PUXANDO MULTIPLAS LINHAS
print(df.loc[['B', 'E'],['W', 'X', 'Y', 'Z']])
print(df.iloc[[1, 4], :])

#PUXANDO A MATRIZ 2X2 DO CANTO INFERIOR DIREITO
print(df.loc[['D', 'E'],['Y', 'Z']])
print(df.iloc[[3, 4], [2, 3]])