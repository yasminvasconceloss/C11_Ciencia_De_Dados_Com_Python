#LISTAS
#Guarda um conjunto de elementos ----> entre []
#Coleção MUTÁVEL de dados
#Permite inserir, alterar, navegar
#Permite SLICING

nomes = ['Goku', 'Vegeta', 'Trunks', 'Gohan']
print(nomes)
print(type(nomes)) #tipo da variavel

#--------------CRUD DE DADOS NA LISTA----------------

#CREATE -> criar
nomes.append('Majin Boo') #APPEND -> adiciona no final
nomes.insert(2, 'Piccolo') #inserir > primeiro o índice e depois a inserção
print(nomes)

#READ -> ler, mesmo procedimento da tupla

#UPDATE -> atualizar
nomes[0] = 'Tenshin Han'
print(nomes)

#DELETE -> deletar
del nomes[1] #deletando pelo índice
nomes.remove('Trunks') #REMOVE -> deletando pelo valor
print(nomes)