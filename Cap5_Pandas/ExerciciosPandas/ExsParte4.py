import pandas as pd

# Dataset paises.csv
paises = pd.read_csv('paises.csv', sep=';')


# 6. Agrupe os países por região e mostre as estatísticas
# descritivas da coluna Population de cada região.
# Em seguida, mostre apenas as 5 primeiras linhas deste resultado.

# groupby() -> agrupa os países por região.
# describe() -> mostra as estatísticas descritivas da população.
# head(5) -> mostra apenas as 5 primeiras linhas.

estatisticas_populacao = paises.groupby('Region')['Population'].describe()
print(estatisticas_populacao.head(5))



# 7. Crie uma função que receba a coluna
# Infant mortality (per 1000 births) de um país
# e retorne o valor reduzido em 15%.
# Aplique esta função à coluna usando o
# método apply() e, em seguida, concatene a coluna original com a coluna
# resultante lado a lado para se fazer uma comparação;

def reduzir_mortalidade(valor):
    return valor * 0.85

# Aplica a função em cada valor da coluna
mortalidade_reduzida = paises['Infant mortality (per 1000 births)'].apply(
    reduzir_mortalidade
)

# Junta a coluna original e a coluna reduzida lado a lado
comparacao = pd.concat(
    [
        paises['Infant mortality (per 1000 births)'],
        mortalidade_reduzida
    ],
    axis=1
)


# Renomeando as colunas para facilitar a comparação
comparacao.columns = [
    'Mortalidade Original',
    'Mortalidade Reduzida'
]

print(comparacao)



# 8. Remova a coluna Coastline (coast/area ratio) do Dataset.
# Em seguida, salve este novo Dataset em um arquivo chamado
# paises_sem_coastline.csv.
#
# drop() -> remover a coluna Coastline.
# to_csv() para salvar o novo Dataset.

paises_sem_coastline = paises.drop(
    columns=['Coastline (coast/area ratio)']
)

# Salva o novo Dataset em um arquivo CSV
paises_sem_coastline.to_csv(
    'paises_sem_coastline.csv',
    sep=';',
    index=False
)

print(paises_sem_coastline)