#Exercicio 1

nome = "Yasmin Vasconcelos"
print(nome.upper()) #Todas as letras maiusculas
print(nome.lower()) #Todas as letras minusculas
print(len(nome) - nome.count(" ")) #quantidade de letras do nome
print(nome.replace("Vasconcelos", "do Inatel"))


#Exercicio 2

numero = int(input("Digite o número da tabuada: "))
inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

for i in range(inicio, fim + 1):
    print(numero, "x", i, "=", numero * i)


#Exercicio 3

sexo = input("Digite o sexo (M ou F): ")

while sexo != "M" and sexo != "F" and sexo != "m" and sexo != "f":
    print("Sexo inválido!")
    sexo = input("Tente Novamente (M ou F): ")

if sexo == "M" or sexo == "m":
    print("Homem")
else:
    print("Mulher")

