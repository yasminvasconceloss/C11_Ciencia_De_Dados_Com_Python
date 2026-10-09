import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 5. Utilizando o dataset paises.csv, calcule a correlação entre
# "GDP ($ per capita)", "Literacy (%)",
# "Infant mortality (per 1000 births)" e "Phones (per 1000)",
# apresentando o resultado em um Heatmap com os valores numéricos exibidos.

# Carrega o dataset
paises = pd.read_csv('paises.csv', sep=';')

# Retira espaços extras dos nomes das colunas
paises.columns = paises.columns.str.strip()

# Seleciona as variáveis desejadas
dados = paises[
    [
        'GDP ($ per capita)',
        'Literacy (%)',
        'Infant mortality (per 1000 births)',
        'Phones (per 1000)'
    ]
]

# Calcula a correlação
correlacao = dados.corr()

# Exibe os valores das correlações
print(correlacao)

# Cria o Heatmap
sns.heatmap(correlacao, annot=True, cmap='coolwarm', vmin=-1, vmax=1)

plt.title('Correlação entre indicadores dos países')
plt.show()




# 6. Com o dataset paises.csv, trace um Boxplot comparando
# a distribuição do "GDP ($ per capita)" entre os países da
# América Latina e da Europa Ocidental, permitindo identificar
# mediana, dispersão e outliers de cada grupo.

# Carrega o dataset
paises = pd.read_csv('paises.csv', sep=';')

# Retira espaços extras dos nomes das colunas
paises.columns = paises.columns.str.strip()

# Retira espaços extras dos valores da região
paises['Region'] = paises['Region'].str.strip()

# Seleciona as duas regiões
regioes = paises[
    paises['Region'].isin([
        'LATIN AMER. & CARIB',
        'WESTERN EUROPE'
    ])
]

# Cria o Boxplot
sns.boxplot(
    data=regioes,
    x='Region',
    y='GDP ($ per capita)'
)

plt.title('GDP por região')
plt.xlabel('Região')
plt.ylabel('GDP per capita')

plt.xticks(rotation=15)
plt.show()




# 7. Utilizando o dataset paises.csv, trace um Regplot relacionando
# a taxa de alfabetização (Literacy (%)) com a mortalidade infantil
# (Infant mortality (per 1000 births)), customizando a cor
# da linha de regressão.


# Carrega o dataset
paises = pd.read_csv('paises.csv', sep=';')

# Retira espaços extras dos nomes das colunas
paises.columns = paises.columns.str.strip()

# Cria o Regplot
sns.regplot(
    data=paises,
    x='Literacy (%)',
    y='Infant mortality (per 1000 births)',
    line_kws={'color': 'red'}
)

plt.title('Alfabetização x Mortalidade infantil')
plt.xlabel('Taxa de alfabetização (%)')
plt.ylabel('Mortalidade infantil')

plt.show()




# 8. Por meio do dataset space.csv, após filtrar apenas as missões
# com custo conhecido (Cost > 0), trace um Boxplot comparando
# a distribuição do custo das missões (Cost) entre foguetes com
# status "StatusActive" e "StatusRetired", permitindo identificar
# mediana, dispersão e outliers de cada grupo.


# Carrega o dataset
space = pd.read_csv('space.csv', sep=';')

# Retira espaços extras dos nomes das colunas
space.columns = space.columns.str.strip()

# Retira espaços extras da coluna Status Rocket
space['Status Rocket'] = space['Status Rocket'].str.strip()

# Converte o custo para número
space['Cost'] = pd.to_numeric(space['Cost'], errors='coerce')

# Seleciona somente missões com custo maior que zero
space = space[space['Cost'] > 0]

# Cria o Boxplot
sns.boxplot(
    data=space,
    x='Status Rocket',
    y='Cost'
)

plt.title('Custo das missões por status do foguete')
plt.xlabel('Status do foguete')
plt.ylabel('Custo da missão')

plt.show()