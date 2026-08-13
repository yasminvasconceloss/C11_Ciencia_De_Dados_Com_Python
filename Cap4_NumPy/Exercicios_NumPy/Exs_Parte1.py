"""1. Crie dois NumPy Arrays unidimensionais de tamanho 8: um formado apenas por 1’s
e outro formado por números aleatórios entre 0 e 9. Some estes dois NumPy Arrays
e guarde o resultado dentro de um terceiro NumPy Array. Por fim, faça o seguinte:
a. Se a soma de todos os elementos do Array resultante for >= 40 , remodele este
NumPy Array para se tornar uma matriz com mais linhas do que colunas. Senão,
remodele para que se torne uma matriz com mais colunas do que linhas."""

import numpy as np

array1 = np.full(8,1) #criando array unidimensional
array2 = np.random.randint(1, 10, 8)
print(array1)
print(array2)

array3 = array1 + array2 #soma dos arrays
print(array3)

if np.sum(array3) >= 40:
    mtz = array3.reshape(4, 2)
else:
    mtz = array3.reshape(2, 4)

print(mtz)



'''2. Crie dois NumPy Arrays unidimensionais: um de números pares de 0 à 51
e outro também de números pares de 100 até 50. Em seguida, os concatene
e mostre os resultados ordenados. '''

import numpy as np

array1 = np.arange(0, 51, 2)
array2 = np.arange(100, 50, -2)

array3 = np.concatenate([array1, array2])
print(np.sort(array3))


'''3. Mini Campo Minado
    a) Crie um NumPy Array 2 x 2 formado apenas por 0’s
    b) Em seguida, adicione um número 1 em uma posição aleatória desta matriz;
    c) Faça uma entrada de dados para solicitar o usuário que faça uma jogada (selecione uma posição da matriz) 
        I. Se ele selecionar todas as posições em que o número 1 não se encontra, mostre a mensagem
           “Congratulations ! You beat the game!:)”
        II. Senão, se dentro das 3 primeiras jogadas ele achar o número 1, mostre a mensagem
            “Game Over!:( Try Again!”   '''

import numpy as np  # Importa a biblioteca NumPy

#Criando matriz 2x2 formada apenas com zeros
campo = np.zeros((2, 2), dtype=int)

linha_bomba = np.random.randint(0, 2) #Escolhendo aleatoriamente uma linha entre 0 e 1
coluna_bomba = np.random.randint(0, 2) #             ""              coluna entre 0 e 1
campo[linha_bomba, coluna_bomba] = 1 # 1 na posição sorteada
print(campo)

jogadas = np.zeros((2, 2), dtype=int) #matriz 2x2 para guardar as posições que o jogador já escolheu
contador = 0 #quantidade de jogadas já feitas

# Enquanto o jogador não fizer 4 jogadas, o jogo continua
while contador < 4:

    linha = int(input("Escolha uma linha (0 ou 1): "))

    coluna = int(input("Escolha uma coluna (0 ou 1): "))

    # Verificando se a posição escolhida já foi jogada
    if jogadas[linha, coluna] == 1:
        print("Posição já selecionada! Escolha outra.")
        continue  # Voltando para o início do while sem contar essa jogada

    jogadas[linha, coluna] = 1  # Marca a posição escolhida pelo jogador como já utilizada

    contador = contador + 1

    # Verifica se o jogador encontrou o número 1
    if campo[linha, coluna] == 1:

        if contador <= 3:
            print("Game Over!:( Try Again!")
        break

    # Se o jogador não encontrou o 1
    else:

        # Verifica se ele já escolheu as outras 3 posições
        if contador == 3:
            print("Congratulations ! You beat the game!:)")
            break