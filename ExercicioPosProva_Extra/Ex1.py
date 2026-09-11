# Crie um programa que leia o nome e ano de várias músicas
# (até que o usuário não queira mais cadastrar),
# guardando os dados de cada música em um dicionário
# e todos os dicionários em uma lista. No final, mostre:
# a. Quantas músicas foram cadastradas;
# b. As informações da(s) música(s) do ano mais antigo.

musicas = []

while True:
    nome = input('Digite o nome da música: ')
    ano = int(input('Digite o ano da música: '))

    musica = {
        'nome': nome,
        'ano': ano
    }

    musicas.append(musica)

    continuar = input('Deseja cadastrar outra música? (s/n): ')

    if continuar == 'n':
        break

# Quantidade de músicas cadastradas
print('\nQuantidade de músicas cadastradas:', len(musicas))

# Música(s) do ano mais antigo
anoMaisAntigo = min(musica['ano'] for musica in musicas)

print('\nMúsica(s) do ano mais antigo:')

for musica in musicas:
    if musica['ano'] == anoMaisAntigo:
        print('Nome:', musica['nome'])
        print('Ano:', musica['ano'])