#1. Crie uma lista preenchida com os 5 primeiros colocados de um Campeonato de Futebol, na ordem de colocação, depois mostre:

PrimeirosColocados = ['Brasil', 'Alemanha', 'Paris Saint-Germain', 'Barcelona', 'Arsenal']
print(PrimeirosColocados)

print(PrimeirosColocados[0:3]) #a. Apenas os 3 primeiros colocados;
print(PrimeirosColocados[3:]) #b. Os últimos 2 colocados;
print(sorted(PrimeirosColocados))#c. Uma lista com os times em ordem alfabética;

posicao = 0

for time in PrimeirosColocados:   #d. Em que posição da tabela se encontra o Barcelona;
    if time == 'Barcelona':
        print(posicao)
        break
    posicao += 1


#2. Crie dois conjuntos, um para cada loja . Identifique quais modelos de smartphones cada uma delas vendem.
# Em seguida, mostre quais modelos no total você terá opção de comprar se visita-las e quais
#modelos se encontram disponíveis em ambas as lojas;

ModelosLoja1 = {'Iphone 16', 'Iphone 16 pro max', 'Iphone 15 plus', 'Galaxy s25'}
ModelosLoja2 = {'Galaxy s25', 'Galaxy s26 fe', 'Galaxy s21', 'iphone 15 plus'}

total_modelos = ModelosLoja1 | ModelosLoja2
print(f'Modelos disponiveis: {total_modelos}')

modelo_em_ambas = ModelosLoja1 & ModelosLoja2
print(f'Os modelos disponiveis em ambas as lojas são: {modelo_em_ambas}')


#3. Faça um programa que leia o nome e a média de um aluno e guarde-os em um dicionário. Em seguida,
#a partir da média (para ser aprovado deve ter média >=50), gere a situação final do aluno
# (‘AP’ ou ‘RP’), que também deve ser guardada neste dicionário. No final, mostre todo o conteúdo deste dicionário;

nome = str(input('Nome do aluno: '))
media = float(input('Média do aluno: '))

aluno = {
    'nome': nome,
    'media': media
}

print(aluno)

    if media >= 50:
        situacao = 'AP'
    else:
        situacao = 'RP'

aluno['situação'] = situacao

print(aluno)

