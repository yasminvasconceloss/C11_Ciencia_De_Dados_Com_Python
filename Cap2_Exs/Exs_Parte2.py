import math

#Exercicio 4

distancia = float(input("Digite a distância da viagem em km:"))

if distancia <= 200:
    preco = distancia * 0.50

else:
    preco = distancia * 0.45

print("O preço da passagem é de: R$", preco)

#Exercicio 5

numero = int(input("Digite um número entre 1000 e 9999: "))

unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = (numero // 1000) % 10

print("Unidade:", unidade)
print("Dezena:", dezena)
print("Centena:", centena)
print("Milhar:", milhar)

#Exercicio 6

numero = float(input("Digite um número decimal: "))

print("Raiz quadrada:", math.sqrt(numero))
print("Teto:", math.ceil(numero)) #Arredonda o valor para cima, sempre para o menor inteiro maior ou igual ao número.
print("Chão:", math.floor(numero)) #Arredonda o valor para baixo, sempre para o maior inteiro menor ou igual ao número.
print("Parte inteira:", int(numero))

