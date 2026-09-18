import pandas as pd

df = pd.DataFrame(
    {
        "W": [10, 29, 30, 43, 37],
        "X": [37, 26, 9, 41, 48],
        "Y": [16, 30, 10, 37, 12],
        "Z": [1, 49, 1, 17, 25]
    },
    index=["A", "B", "C", "D", "E"]
)

print(df)

# QUESTÃO 6
# Utilizando o DataFrame exemplo do tópico 5.3 deste material,
# calcule a média dos elementos da coluna X que são menores que 30.

valores_x_menores_30 = df.loc[df["X"] < 30, "X"]
media = valores_x_menores_30.mean()

print(valores_x_menores_30)
print("A Média dos elementos da coluna X que são menores que 30 é:", media)



# QUESTÃO 7
# Utilizando o mesmo DataFrame, apresente a média dos elementos
# da linha D usando a função loc() como base e a soma dos elementos
# da linha E usando a função iloc() como base.

media_linha_d = df.loc["D"].mean()
soma_linha_e = df.iloc[4].sum()

print("Média da linha D:", media_linha_d)
print("Soma da linha E:", soma_linha_e)



# QUESTÃO 8
# Faça um Slicing na matriz mostrando apenas as linhas A, C e E
# juntamente com as colunas X e Y. Em seguida, mostre qual seria
# a soma dos elementos de cada uma destas linhas e cada uma destas colunas.

recorte = df.loc[["A", "C", "E"], ["X", "Y"]]

print("DataFrame após o slicing:")
print(recorte)

soma_das_linhas = recorte.sum(axis=1)
soma_das_colunas = recorte.sum(axis=0)

print("\nSoma de cada linha:")
print(soma_das_linhas)

print("\nSoma de cada coluna:")
print(soma_das_colunas)
