import numpy as np
import pandas as pd

#Como preencher uma Series
#Lista de labels
#Lista de Valores

labels = ['Tiago', 'Mateus', 'Bruna', 'Julia']
valores = [23, 25, 27, 22]

#Criando a Series
se1 = pd.Series(index=labels, data=valores)
print(se1)
print(type(se1))

#Acessando elementos da Series
print(se1['Mateus']) #valor guardado em "Mateus"
print(se1[['Mateus', 'Julia']])

#OPERACOES ENTRE SERIES
s1 = pd.Series({'v1':10, 'v2':45, 'v3': 70})
s2 = pd.Series({'v1':10, 'v2':50, 'v3': 70})

#print(s1)
#print(s2)
print(s1+s2)
print(s1.add(s2, fill_value=0))