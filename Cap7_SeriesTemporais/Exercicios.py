
# ============================================================
# QUESTÃO 1
# Por meio dos datasets airtravel.csv e co2_emissions.csv,
# trace suas Séries Temporais.
#
# Em seguida, para cada uma das Séries, realize a sua
# decomposição e responda às seguintes perguntas:
#
# a. A série possui Tendência? Se sim, que tipo?
# b. A série possui Sazonalidade? Se sim, qual o período
#    que ela acontece?
# c. A série apresenta um Ciclo? Se sim, por qual razão?
#
# Obs: após a plotagem e decomposição das séries, responda
# às perguntas por meio de comentários no próprio código.
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose



# EXERCÍCIO 1 - AIRTRAVEL.CSV


# parse_dates transforma a coluna Date em formato de data
# index_col define Date como índice da série temporal

airtravel = pd.read_csv(
    'airtravel.csv',
    parse_dates=['Date'],
    index_col='Date'
)

# Garantindo que os valores de passageiros sejam numéricos

airtravel['Passengers'] = pd.to_numeric(
    airtravel['Passengers'], errors='coerce'
)

# Organizando os dados pela data e definindo a frequência mensal

airtravel = airtravel.sort_index()
airtravel = airtravel.asfreq('MS')


# Plotando a série temporal origina

airtravel['Passengers'].plot(
    figsize=(10, 5),
    title='Número de passageiros ao longo do tempo',
    xlabel='Data',
    ylabel='Número de passageiros'
)

plt.tight_layout()
plt.show()


# Realizando a decomposição da série temporal.
# Modelo multiplicativo: utilizado quando a variação sazonal
# aumenta proporcionalmente ao crescimento da tendência
# period=12 -> repetição a cada 12 meses

decomposition_airtravel = seasonal_decompose(
    airtravel['Passengers'],
    model='multiplicative',
    period=12
)

# Plotando os componentes da decomposição.

decomposition_airtravel.plot(figsize=(10, 8))
plt.suptitle('Decomposição da Série Temporal - Airtravel', y=1.02)
plt.tight_layout()
plt.show()


# RESPOSTAS:

# a) A série possui tendência crescente, pois o número de
# passageiros aumenta ao longo dos anos, apresentando
# crescimento aproximadamente linear.

# b) A série apresenta sazonalidade com período de 12 meses.
# Os maiores números de passageiros ocorrem principalmente
# nos meses de julho e agosto, repetindo esse comportamento
# nos anos analisados.

# c) Não é possível identificar um ciclo de longo prazo,
# pois o dataset apresenta apenas 3 anos de observações.
# As oscilações observadas estão relacionadas principalmente
# à sazonalidade anual.



# EXERCÍCIO 2 - CO2_EMISSIONS.CSV


# Carregando o dataset

co2 = pd.read_csv('co2_emissions.csv')

# Transformando a coluna Year em formato de data

co2['Year'] = pd.to_datetime(
    co2['Year'].astype(str),
    format='%Y'
)

# Definindo Year como índice da série temporal

co2 = co2.set_index('Year')

# Garantindo que os valores de emissão sejam numéricos

co2['CO2_Emissions'] = pd.to_numeric(
    co2['CO2_Emissions'], errors='coerce'
)

# Organizando os dados e definindo a frequência anual

co2 = co2.sort_index()
co2 = co2.asfreq('YS')


# Plotando a série temporal original

co2['CO2_Emissions'].plot(
    figsize=(10, 5),
    title='Emissões de CO2 ao longo dos anos',
    xlabel='Ano',
    ylabel='Emissões de CO2'
)

plt.tight_layout()
plt.show()


# Realizando a decomposição da série temporal.
# Modelo aditivo: utilizado quando as variações apresentam
# uma amplitude aproximadamente constante.
# period=8 -> padrão de repetição de aproximadamente
# 8 anos, observado nas oscilações dos dados anuais.

decomposition_co2 = seasonal_decompose(
    co2['CO2_Emissions'],
    model='additive',
    period=8
)

# Plotando os componentes da decomposição.

decomposition_co2.plot(figsize=(10, 8))
plt.suptitle('Decomposição da Série Temporal - CO2', y=1.02)
plt.tight_layout()
plt.show()


# RESPOSTAS:

# a) A série possui tendência decrescente, aproximadamente
# linear, pois as emissões apresentam uma redução ao longo
# dos anos, apesar de algumas oscilações.

# b) A série não apresenta sazonalidade intra-anual, pois
# os dados são registrados apenas uma vez por ano.
# Entretanto, apresenta oscilações periódicas ao longo
# dos anos, com um padrão aproximado de 8 anos.

# c) A série apresenta ciclos de aproximadamente 8 anos,
# caracterizados por períodos de crescimento e diminuição
# das emissões de CO2. Essas oscilações podem estar relacionadas
# a diferentes fatores que influenciam as emissões ao longo
# do tempo.
