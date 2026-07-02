#Faça um Programa que leia três números e mostre o maior deles
primeiro_numero = float(input("Digite o 1º número: "))
segundo_numero = float(input("Digite o 2º número: "))
terceiro_numero = float(input("Digite o 3º número: "))
if primeiro_numero == segundo_numero and primeiro_numero == terceiro_numero:
    print("Todos os números são iguais")
elif primeiro_numero > segundo_numero and primeiro_numero > terceiro_numero:
    print("O primeiro número é o Maior")
elif segundo_numero > primeiro_numero and segundo_numero > terceiro_numero:
    print("O segundo número é o Maior")
elif terceiro_numero > primeiro_numero and terceiro_numero > segundo_numero:
    print("O terceiro número é o Maior")