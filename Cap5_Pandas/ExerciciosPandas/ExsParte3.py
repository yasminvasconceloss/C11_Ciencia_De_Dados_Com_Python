import pandas as pd

# 1. Carregue o Dataset paises.csv e mostre:
# a) Quais são os países da OCEANIA;
# b) Quantos países são da OCEANIA.

#.str.contains() -> para procurar "OCEANIA" dentro da coluna Region.
paises = pd.read_csv('paises.csv', sep=';')
oceania = paises[paises['Region'].str.contains('OCEANIA', na=False)]

# Mostra os países da OCEANIA
print(oceania['Country'])

# Mostra a quantidade de países da OCEANIA
print('Quantidade de países da OCEANIA:', len(oceania))



# 2. Encontre o nome e a região do país que possui
# a maior população segundo este Dataset.


#.idxmax() -> para encontrar o índice da maior população.
maior_populacao = paises['Population'].idxmax()
print(paises.loc[maior_populacao, ['Country', 'Region']])



# 3. Agrupe os países por Regiões.
# Em seguida, mostre a média de alfabetização (Literacy (%))
# de cada região do planeta.


#groupby() -> agrupar os países pela coluna Region
#mean() -> calcular a média da coluna Literacy (%).
media_alfabetizacao = paises.groupby('Region')['Literacy (%)'].mean()
print(media_alfabetizacao)



# 4. Busque o nome de todos os países que não possuem
# costa marítima (Coastline (coast/area ratio) == 0)
# e guarde-os em um novo arquivo chamado noCoast.csv.

sem_costa = paises[paises['Coastline (coast/area ratio)'] == 0] #filtrando os países cuja coluna Coastline é igual a 0.

# Mostra os nomes dos paises
print(sem_costa['Country'])

# Salvando os países sem costa no arquivo noCoast.csv
sem_costa.to_csv('noCoast.csv', sep=';', index=False)


# 5. Faça uma função que receba a taxa de mortalidade
# de cada país (Deathrate) e retorne:
# 'Balanced' caso o valor seja menor que 9
# 'Urgent' caso contrário.
#Em seguida, crie um campo no Dataset chamado
# ‘Humanitarian Help’ que receba estes valores para cada país.
# No final, mostre o Dataset para verificar se a inserção da nova
#coluna foi feita com sucesso.

def classificacao_mortalidade(deathrate):
    if deathrate < 9:
        return 'Balanced'
    else:
        return 'Urgent'


paises['Humanitarian Help'] = paises['Deathrate'].apply(classificacao_mortalidade)

# Mostra o Dataset para verificar a nova coluna
print(paises)