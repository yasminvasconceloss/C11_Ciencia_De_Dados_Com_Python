# 5. Por meio do dataset paises.csv, trace um gráfico de dispersão
# relacionando a renda per capita (GDP ($ per capita)) com a taxa de
# alfabetização (Literacy (%)) dos países da América Latina.
# Além disso, faça com que o tamanho de cada ponto represente a população do país.

import pandas as pd
import matplotlib.pyplot as plt

# Carrega o dataset
paises = pd.read_csv('paises.csv', sep=';')

# Retira espaços extras dos nomes das colunas
paises.columns = paises.columns.str.strip()

# Retira espaços extras da coluna Region
paises['Region'] = paises['Region'].str.strip()

# Seleciona os países da América Latina
america_latina = paises[
    paises['Region'].str.contains('LATIN AMER', case=False, na=False)
]

# Cria o gráfico de dispersão
plt.figure(figsize=(10, 6))

plt.scatter(
    america_latina['GDP ($ per capita)'],
    america_latina['Literacy (%)'],
    s=america_latina['Population'] / 100000,
    alpha=0.6
)

plt.title('GDP x Alfabetização - América Latina')
plt.xlabel('GDP ($ per capita)')
plt.ylabel('Literacy (%)')

plt.grid()
plt.show()



# 6. Com base nos dados do dataset space.csv, trace um gráfico em torta
# ilustrando a porcentagem geral de foguetes com status "StatusActive"
# e "StatusRetired", considerando todas as empresas.

# Carrega o dataset
space = pd.read_csv('space.csv', sep=';')

# Retira espaços extras dos nomes das colunas
space.columns = space.columns.str.strip()

# Retira espaços extras da coluna Status Rocket
space['Status Rocket'] = space['Status Rocket'].str.strip()

# Conta a quantidade de foguetes ativos e aposentados
status = space['Status Rocket'].value_counts()

# Cria o gráfico de torta
plt.figure(figsize=(7, 7))

plt.pie(
    status,
    labels=status.index,
    autopct='%1.1f%%'
)

plt.title('Status dos Foguetes')

plt.show()



# 7. Por meio do dataset paises.csv, trace em um mesmo plano cartesiano
# duas linhas com estilos customizados (marcador, cor e tipo de linhas
# diferentes) comparando o "GDP ($ per capita)" e o número de
# "Phones (per 1000)" dos países da Europa Ocidental (WESTERN EUROPE).


# Carrega o dataset
paises = pd.read_csv('paises.csv', sep=';')

# Retira espaços extras dos nomes das colunas
paises.columns = paises.columns.str.strip()

# Retira espaços extras da coluna Region
paises['Region'] = paises['Region'].str.strip()

# Seleciona os países da Europa Ocidental
europa_ocidental = paises[
    paises['Region'] == 'WESTERN EUROPE'
]

# Cria o gráfico
plt.figure(figsize=(10, 6))

# Linha do GDP
plt.plot(
    europa_ocidental['Country'],
    europa_ocidental['GDP ($ per capita)'],
    marker='o',
    linestyle='-',
    color='blue',
    label='GDP per capita'
)

# Linha dos telefones
plt.plot(
    europa_ocidental['Country'],
    europa_ocidental['Phones (per 1000)'],
    marker='s',
    linestyle='--',
    color='red',
    label='Phones por 1000'
)

plt.title('GDP x Telefones - Europa Ocidental')
plt.xlabel('País')
plt.ylabel('Valor')
plt.xticks(rotation=45)

plt.legend()
plt.grid()

plt.show()


# 8. Por meio do dataset space.csv, usando o conceito de subplot(),
# trace dois gráficos de barras separados lado a lado:
# à esquerda, as 5 empresas com mais missões de sucesso;
# à direita, as 5 empresas com mais missões de falha.

# Carrega o dataset
space = pd.read_csv('space.csv', sep=';')

# Retira espaços extras dos nomes das colunas
space.columns = space.columns.str.strip()

# Retira espaços extras da coluna Status Mission
space['Status Mission'] = space['Status Mission'].str.strip()

# Seleciona as missões de sucesso
sucessos = space[
    space['Status Mission'] == 'Success'
]

# Conta as 5 empresas com mais missões de sucesso
top5_sucessos = sucessos['Company Name'].value_counts().head(5)

# Seleciona as missões de falha
falhas = space[
    space['Status Mission'] == 'Failure'
]

# Conta as 5 empresas com mais missões de falha
top5_falhas = falhas['Company Name'].value_counts().head(5)

# Cria dois gráficos lado a lado
plt.figure(figsize=(14, 5))

# Gráfico da esquerda - Sucessos
plt.subplot(1, 2, 1)

top5_sucessos.plot(kind='bar')

plt.title('5 Empresas com Mais Sucessos')
plt.xlabel('Empresa')
plt.ylabel('Quantidade de missões')
plt.xticks(rotation=45)

# Gráfico da direita - Falhas
plt.subplot(1, 2, 2)

top5_falhas.plot(kind='bar')

plt.title('5 Empresas com Mais Falhas')
plt.xlabel('Empresa')
plt.ylabel('Quantidade de missões')
plt.xticks(rotation=45)

# Ajusta o espaço entre os gráficos
plt.tight_layout()

plt.show()


