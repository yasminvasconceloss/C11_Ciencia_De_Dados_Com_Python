#Questão 1
#Mostre qual a média de idade das mulheres presentes neste dataset

import numpy as np
dataset = np.loadtxt('shopping_trends.csv', delimiter=',', dtype=str, encoding='utf-8')
#print(dataset)

dados = dataset[1:]
genero = dados[:,2]
idades = dados[:,1]
#print(genero)
#print(idades)

idadesMulheres = idades[genero == 'Female'].astype(int)

print('A média da idades das mulheres e de:', np.mean(idadesMulheres))




#Questão 2
#Mostre quantos clientes homens gastaram mais que a média de gastos das compras deste dataset

dados = dataset[1:]
genero = dados[:,2]
gastos = dados[:,5].astype(float)
#print(genero)
#print(gastos)


media = np.mean(gastos) #media dos gastos
homens = gastos[genero == 'Male']
quantidade = np.sum(homens > media)

print('A quantidade de clientes homens que gastaram mais que a média de gastos das compras é de:', quantidade)




# Questão 3
# Mostre a porcentagem de vendas do item menos vendido da loja

dados = dataset[1:]
itens = dados[:,3]
#print(itens)

valores, quantidades = np.unique(itens, return_counts=True)
menorQuantidade = np.min(quantidades)
porcentagem = (menorQuantidade / len(itens))*100

print('A porcntagem de vendas do item menos vendido da loja é de:', porcentagem, '%')




#Questão 4
#Mostre qual a porcentagem de vendas que tiveram algum tipo de desconto

dados = dataset[1:]
descontos = dados[:, 13] #Discount Applied
#print(descontos)

quantidade = np.sum(descontos == 'Yes')
porcentagem = (quantidade / len(descontos))*100

print('A porcentagem de vendas que tiveram algum tipo de desconto é de:', porcentagem, '%')





#Questão 5
#Mostre qual a cor de roupa mais popular no verão segundo esse dataset

dados = dataset[1:]
estacao = dados[:,9]
cores = dados[:,8]
#print(estacao)
#print(cores)

coresVerao = cores[estacao == 'Summer'] #verao
valores, quantidades = np.unique(coresVerao, return_counts=True)
maisPopular = valores[np.argmax(quantidades)]

print('A cor da roupa mais popular do verão é:', maisPopular)


