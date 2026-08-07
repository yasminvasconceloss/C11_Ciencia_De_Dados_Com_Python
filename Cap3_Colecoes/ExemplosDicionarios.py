#DICIONARIOS
#Organiza seus elementos no padrão: chave e valor
#Coleçao MUTÁVEL

pessoa = {
    'nome':'Goku',
    'idade':52,
    'sexo': 'M'
    }
print(pessoa)
print(type(pessoa))

#--------------CRUD DE DADOS NA LISTA----------------

#CREATE -> criar
pessoa['Desenho'] = 'DBZ'  #ADICIONA
print(pessoa)

#READ -> ler, mesmo procedimento da tupla
print(pessoa['nome']) #valor associado a chave

#UPDATE -> atualizar
pessoa['Desenho'] = 'DBZ'
print(pessoa)

#DELETE -> deletar
del pessoa['sexo']
print(pessoa)