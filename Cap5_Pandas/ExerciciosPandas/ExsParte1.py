import pandas as pd

# QUESTÃO 1
# Crie duas Series com os seguintes valores:
# serieAno1: {'Java': 16.25, 'C': 16.04, 'Python': 9.85}
# serieAno2: {'C': 16.21, 'Python': 12.12, 'Java': 11.68}

serieAno1 = pd.Series({
    'Java': 16.25,
    'C': 16.04,
    'Python': 9.85
})

serieAno2 = pd.Series({
    'C': 16.21,
    'Python': 12.12,
    'Java': 11.68
})

print("Série Ano 1:")
print(serieAno1)

print("\nSérie Ano 2:")
print(serieAno2)



# QUESTÃO 2
# Os valores das Series representam as fatias de mercado
# (porcentagem) de 3 linguagens de programação populares em
# dois anos consecutivos.
#
# Para cada ano, apresente a porcentagem total que elas juntas
# representam no mercado.

totalAno1 = serieAno1.sum()
totalAno2 = serieAno2.sum()

print("\nTotal do Ano 1:", totalAno1, "%")
print("Total do Ano 2:", totalAno2, "%")



# ============================================================
# QUESTÃO 3
# Apresente o crescimento/declínio no mercado de cada
# linguagem do primeiro ano para o segundo ano.
# ============================================================

crescimento = serieAno2 - serieAno1

print("\nCrescimento/Declínio:")
print(crescimento)



# QUESTÃO 4
# Baseado nos resultados da Questão 3, mostre apenas os dados
# das linguagens que tiveram crescimento.

linguagensCresceram = crescimento[crescimento > 0]

print("\nLinguagens que tiveram crescimento:")
print(linguagensCresceram)



# QUESTÃO 5
# Se estas porcentagens de crescimento/declínio se mantivessem
# iguais para os próximos 2 anos, qual seria a linguagem mais
# popular?
# Dica: use o método nlargest(1) no final para retornar
#  rapidamente a label e o maior valor de uma Series.

ano3 = serieAno2 + crescimento
ano4 = ano3 + crescimento

print("\nProjeção para o Ano 3:")
print(ano3)

print("\nProjeção para o Ano 4:")
print(ano4)

maisPopular = ano4.nlargest(1)

print("\nLinguagem mais popular:")
print(maisPopular)