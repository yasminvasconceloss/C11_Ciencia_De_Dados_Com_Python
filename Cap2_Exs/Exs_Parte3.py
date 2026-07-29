#Exercicio 7

palavra = input("Digite uma palavra: ")

vogais = 0
tem_a = False

for letra in palavra:
    print(letra.upper())

    if letra.upper() == "A":
        tem_a = True

    if letra.upper() in "AEIOU":
        vogais = vogais + 1

print("Quantidade de vogais:", vogais)

if tem_a:
    print("Tem a letra A na palavra")
else:
    print("Não tem a letra A na palavra)



#Exercicio 8

Numero1 = int(input("Digite o primeiro numero:"))
Numero2 = int(input("Digite o segundo numero:"))

adicao = Numero1 + Numero2
print("A soma dos numeros é: ", adicao)

subtracao = Numero1 - Numero2
print("A subtração dos números é: ", subtracao)

multiplicacao = Numero1 * Numero2
print("A multiplicação dos números é: ", multiplicacao)

Resto = Numero1 % Numero2
print("O resto da divisão é: ", Resto)

potencia = Numero1 ** Numero2
print("O primeiro número elevado ao segundo número é: ", potencia)