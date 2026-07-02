#Faça um Programa que leia três números e mostre o maior e o menor deles.
primeiro_numero = float(input("Digite o 1º número: "))
segundo_numero = float(input("Digite o 2º número: "))
terceiro_numero = float(input("Digite o 3º número: "))
if primeiro_numero == segundo_numero and primeiro_numero == terceiro_numero:
    print("Todos os números são iguais")
else:
#Validações para identificar o Maior número
    if primeiro_numero >= segundo_numero and primeiro_numero >= terceiro_numero:
        print("O primeiro número e o MAIOR")
    elif segundo_numero >= primeiro_numero and segundo_numero >= terceiro_numero:
        print("O segundo número e o MAIOR")
    elif terceiro_numero >= primeiro_numero and terceiro_numero >= segundo_numero:
        print("O terceiro número e o MAIOR")
#Validaçõs para identificar o Menor número
if primeiro_numero <= segundo_numero and primeiro_numero <= terceiro_numero:
    print("O primeiro número e o MENOR")
elif segundo_numero <= primeiro_numero and segundo_numero <= terceiro_numero:
    print("O segundo número e o MENOR")
elif terceiro_numero <= primeiro_numero and terceiro_numero <= segundo_numero:
    print("O terceiro número e o MENOR")