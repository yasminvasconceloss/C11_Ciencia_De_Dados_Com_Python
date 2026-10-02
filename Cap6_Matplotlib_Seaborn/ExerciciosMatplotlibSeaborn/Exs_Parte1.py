# 1. Por meio do dataset paises.csv, trace dois gráficos de linhas em
# um mesmo plano cartesiano, um mostrando a taxa de mortalidade
# (Deathrate) e outro a taxa de natalidade (Birthrate) dos países dan América do Norte.

import pandas as pd
import matplotlib.pyplot as plt

# Carrega o dataset
paises = pd.read_csv('paises.csv', sep=';')

# Retira espaços extras dos nomes das colunas
paises.columns = paises.columns.str.strip()

# Retira espaços extras da coluna Region
paises['Region'] = paises['Region'].str.strip()

# Seleciona os países da América do Norte
america_norte = paises[paises['Region'] == 'NORTHERN AMERICA']

# Criando o gráfico
plt.figure(figsize=(10, 5))

# Taxa de mortalidade
plt.plot(
    america_norte['Country'],
    america_norte['Deathrate'],
    marker='o',
    label='Mortalidade'
)

# Taxa de natalidade
plt.plot(
    america_norte['Country'],
    america_norte['Birthrate'],
    marker='o',
    label='Natalidade'
)

plt.title('Taxa de Natalidade e Mortalidade - América do Norte')
plt.xlabel('País')
plt.ylabel('Taxa')
plt.xticks(rotation=45)
plt.legend()
plt.grid()

plt.show()


# 2. Por meio do dataset space.csv, trace um gráfico em barras
# mostrando quantas empresas espaciais diferentes os EUA e a CHINA
# possuem. Dica: não se esqueça de retirar os resultados repetidos.

# Carrega o dataset
space = pd.read_csv('space.csv', sep=';')

# Retira espaços extras dos nomes das colunas
space.columns = space.columns.str.strip()

# Seleciona empresas localizadas nos EUA
eua = space[space['Location'].str.contains('USA', case=False, na=False)]

# Seleciona empresas localizadas na China
china = space[space['Location'].str.contains('China', case=False, na=False)]

# Retira empresas repetidas
eua = eua.drop_duplicates(subset=['Company Name'])
china = china.drop_duplicates(subset=['Company Name'])

# Conta a quantidade de empresas
quantidade_eua = len(eua)
quantidade_china = len(china)

# Criando os dados para o gráfico
quantidade = pd.Series(
    [quantidade_eua, quantidade_china],
    index=['EUA', 'China']
)

# Cria o gráfico de barras
plt.figure(figsize=(7, 5))

quantidade.plot(kind='bar')

plt.title('Empresas Espaciais - EUA e China')
plt.xlabel('País')
plt.ylabel('Quantidade de empresas')
plt.xticks(rotation=0)

plt.show()




# 3. Por meio do dataset space.csv, trace um gráfico em torta
# ilustrando a porcentagem de missões da empresa Roscosmos que deram certo e que deram errado.

# Carrega o dataset
space = pd.read_csv('space.csv', sep=';')

# Retira espaços extras dos nomes das colunas
space.columns = space.columns.str.strip()

# Seleciona somente as missões da Roscosmos
roscosmos = space[space['Company Name'] == 'Roscosmos']

# Conta a quantidade de missões por status
status = roscosmos['Status Mission'].value_counts()

# Criando o gráfico de torta
plt.figure(figsize=(7, 7))

plt.pie(
    status,
    labels=status.index,
    autopct='%1.1f%%'
)

plt.title('Missões da Roscosmos')

plt.show()




# 4. Utilizando o dataset space.csv, trace um gráfico em barras com
# as 5 empresas que mais tiveram missões com status "Failure".


# Carrega o dataset
space = pd.read_csv('space.csv', sep=';')

# Retira espaços extras dos nomes das colunas
space.columns = space.columns.str.strip()

# Seleciona somente as missões que falharam
falhas = space[space['Status Mission'] == 'Failure']

# Conta quantas falhas cada empresa teve
quantidade_falhas = falhas['Company Name'].value_counts()

# Seleciona as 5 empresas com mais falhas
top5 = quantidade_falhas.head(5)

# Criando o gráfico de barras
plt.figure(figsize=(9, 5))

top5.plot(kind='bar')

plt.title('5 Empresas com Mais Missões com Status Failure')
plt.xlabel('Empresa')
plt.ylabel('Quantidade de falhas')
plt.xticks(rotation=45)

plt.show()