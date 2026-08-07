#dicionarios
pessoa1 = {'Nome': 'Daniel', 'Cidade':'Muzambinho'}
pessoa2 = {'Nome': 'Leonardo', 'Cidade':'Alfenas'}
pessoa3 = {'Nome': 'Lara', 'Cidade':'SRS'}

#lista
alunos = [pessoa1, pessoa2, pessoa3] #lista de dicionarios

#apenas os dados do leonardo
print(alunos[1])

#apenas a cidade do daniel
print(alunos[0]['Cidade'])

#slicing -> mostrar dados da pessoa 2 para frente
print(alunos[1:])