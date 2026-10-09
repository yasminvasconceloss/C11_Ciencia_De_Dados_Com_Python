import seaborn as sns
import matplotlib.pyplot as plt

# 1. Utilizando o dataset Iris do Seaborn, para os dados apenas da
# espécie 'setosa', avalie a correlação entre suas variáveis numéricas,
# apresentando os valores das correlações e permitindo identificar
# quais variáveis estão mais correlacionadas.


# Carrega o dataset Iris
iris = sns.load_dataset('iris')

# Seleciona somente a espécie setosa
setosa = iris[iris['species'] == 'setosa']

# Calcula a correlação entre as variáveis numéricas
correlacao = setosa.select_dtypes(include='number').corr()

# Exibe os valores das correlações
print(correlacao)

# Cria o mapa de calor
sns.heatmap(correlacao, annot=True, cmap='coolwarm', vmin=-1, vmax=1)

plt.title('Correlação das variáveis - Iris Setosa')
plt.show()




# 2. Utilizando o dataset Titanic, proponha um gráfico que apresente
# a distribuição das idades dos passageiros, diferenciando os dados
# por sexo e incluindo uma curva de densidade (KDE).

# Carrega o dataset Titanic
titanic = sns.load_dataset('titanic')

# Cria o histograma das idades separado por sexo
sns.histplot(
    data=titanic,
    x='age',
    hue='sex',
    kde=True
)

plt.title('Distribuição das idades por sexo - Titanic')
plt.xlabel('Idade')
plt.ylabel('Quantidade de passageiros')

plt.show()



# 3. Utilizando novamente o dataset Titanic, analise a distribuição
# das idades dos passageiros em função da classe, segmentando os dados
# por sexo, de modo a comparar a tendência central, a dispersão e
# possíveis valores extremos entre os grupos.

# Carrega o dataset Titanic
titanic = sns.load_dataset('titanic')

# Cria o gráfico de caixas
sns.boxplot(
    data=titanic,
    x='class',
    y='age',
    hue='sex'
)

plt.title('Distribuição das idades por classe e sexo - Titanic')
plt.xlabel('Classe')
plt.ylabel('Idade')

plt.show()


# 4. Utilizando o dataset mpg, analise a relação entre a potência
# dos veículos (horsepower) e o consumo de combustível (mpg),
# construindo uma visualização que permita identificar a tendência
# entre essas variáveis e interpretar seu comportamento.

# Carrega o dataset MPG
mpg = sns.load_dataset('mpg')

# Cria o gráfico de dispersão com linha de tendência
sns.regplot(
    data=mpg,
    x='horsepower',
    y='mpg'
)

plt.title('Potência x Consumo dos veículos')
plt.xlabel('Potência (horsepower)')
plt.ylabel('Consumo (mpg)')

plt.show()