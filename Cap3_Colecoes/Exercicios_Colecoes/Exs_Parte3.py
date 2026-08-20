#7. Usando a lista de ingredientes já preenchida para a receita de bolo, agora crie
# mais dois conjuntos representando os ingredientes que duas pessoas diferentes têm em casa.
# Mostre quais ingredientes da receita ainda faltam comprar pelas pessoas para se fazer o bolo.

ingredientes = ['Ovo', 'Farinha de trigo', 'Manteiga', 'Leite', 'Açúcar', 'Fermento', 'Cacau em Pó']

ingredientesReceita = set(ingredientes) # passando para conjunto

ingredientesPessoa1 = {'Manteiga', 'Leite'}
ingredientesPessoa2 = {'Cacau em Pó', 'Fermento'}

faltandoPessoa1 = ingredientesReceita - ingredientesPessoa1
print(f'Ingredientes que a pessoa 1 ainda precisa comprar: {faltandoPessoa1}')

faltandoPessoa2 = ingredientesReceita - ingredientesPessoa2
print(f'Ingredientes que a pessoa 1 ainda precisa comprar: {faltandoPessoa2}')




#8. Crie um dicionário para armazenar os dados de um produto (nome, preço e quantidade em estoque).
# Peça ao usuário os dados de 3 produtos diferentes e guarde cada dicionário em uma lista. No final,
# percorra a lista e mostre, para cada produto, seu nome e o valor total em estoque (preço × quantidade).

listaProdutos = []

for i in range(3):
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    quantidade = int(input('Digite a quantidade do produto: '))

    produto = {
        'nome': nome,
        'preço': preco,
        'quantidade': quantidade
    }

    listaProdutos.append(produto)

print(listaProdutos)

for produto in listaProdutos:
    valorTotal = produto['preço'] * produto['quantidade']
    print(f'Produto: {produto['nome']} - Valor total em estoque: {valorTotal:.2f}')