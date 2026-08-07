#TUPLAS
#Guarda um conjunto de elementos ----> entre ()
#É uma coleção IMUTÁVEL, não insere nem altera elementos
#Estados do Brasil em um cadastro por exemplo, coisas que não serão alteradas
#Permite SLICING

nomes = ('Goku', 'Vegeta', 'Trunks', 'Gohan')
print(nomes)
print(type(nomes)) #tipo da variavel

#SLICING DE DADOS ("fatiamento" de dados)
print(nomes)
print(nomes[1])
print(nomes[1:3]) # primeiro argumento é INCLUSIVE e o segundo EXCLUSIVE
print(nomes[1:]) # primeiro em diante
print(nomes[-2]) #varrendo o vetor de trás pra frente