#4. Faça um programa que leia o nome e peso de 3 pessoas e no final mostre o
# nome da pessoa mais pesada e a mais leve;
from tabnanny import process_tokens

nomes = [] #criando listas para guardar nomes e pesos
pesos = []

for i in range(3):  #repetindo 3x o cadastro
    nome = input("Digite o nome: ")
    peso = float(input("Digite o peso: "))

    nomes.append(nome) #adicionando ao final da lista
    pesos.append(peso)

maior = max(pesos) #max -> encontra maior valor dentro de uma lista
menor = min(pesos)

print("Mais pesada:", nomes[pesos.index(maior)]) #index -> procurando a posicao que o valor está
print("Mais leve:", nomes[pesos.index(menor)])



#5. Desenvolva um programa que leia o nome, idade e sexo de n pessoas. No final, mostre:
# a. A média de idade do grupo; b. Quantas mulheres têm menos de 20 anos.
#Dica: em Python, os operadores booleanos básicos são and, or e not.

qtdPessoas = int(input('Entre com o numero de pessoas: '))

pessoas = []

for i in range(qtdPessoas):
    nome = str(input(f'Digite o nome da pessoa {i+1}: '))
    idade = int(input(f'Digite a idade da pessoa {i+1}: '))
    sexo = str(input(f"Escolha o sexo da pessoa {i+1} ('M' e 'F'): ")).upper()

    while sexo != 'M' and sexo != 'F':
        print('Sexo invalido! Escolha M ou F.')
        sexo = str(input(f"Escolha o sexo da pessoa {i+1} ('M' e 'F'): ")).upper()

    pessoas.append([nome, idade, sexo])

print(pessoas)

#Média
somaIdades = 0

for pessoa in pessoas:
    somaIdades += pessoa[1]

media = somaIdades / qtdPessoas

print(f'A média das idades é: {media:.2f}')

# Qtd de mulheres que tem menos de 20 anos

contador = 0
for pessoa in pessoas:
    if(pessoa[2] == 'F' and pessoa[1] < 20 ):
        contador += 1

print(f'A quantidade de mulheres com menos de 20 anos é: {contador}')


#6. Crie uma lista com ingredientes de uma receita de bolo:
# a. Adicione um novo ingrediente no final;
# b. Insira outro em uma posição específica;
# c. Remova um ingrediente pelo valor.

Ingredientes = ['Ovo', 'Farinha de trigo', 'Manteiga', 'Leite']
print(Ingredientes)

Ingredientes.append('Cacau em pó')
print(Ingredientes)

Ingredientes.insert(1, 'Fermento') #inserir > primeiro o índice e depois a inserção
print(Ingredientes)

Ingredientes.remove('Manteiga')
print(Ingredientes)
