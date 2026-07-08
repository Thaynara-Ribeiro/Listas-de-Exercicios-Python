'''Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve
ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.'''
print('''Menu
[1] Soma
[2] Subtração
[3] Multiplicação
[4] Divisão''')
primeiro_numero = float(input("Digite o 1º número: "))
segundo_numero = float(input("Digite o 2º número: "))
escolha = int(input("Digite qual sua escolha: "))
if escolha == 1:
    soma = primeiro_numero + segundo_numero
    if soma % 2 == 0:
        print("O resultado da soma é PAR")
    else:
        print("O resultado da subtração é Impar")
    if soma == round(soma):
        print("O resultado da soma é Inteiro")
    else:
        print("O resultado da soma é Decimal")
    if soma > 0:
        print("O resultado da soma é Positivo")
    else:
        print(f"O resultado da soma é Negativo")

if escolha == 2:
    subtração = primeiro_numero - segundo_numero
    if subtração % 2 == 0:
        print("O resultado da subtração é PAR")
    else:
        print("O resultado da subtração é Impar")
    if subtração == round(subtração):
        print("O resultado da subtração é Inteiro")
    else:
        print("O resultado da subtração é Decimal")
    if subtração > 0:
        print("O resultado da subtração é Positivo")
    else:
        print(f"O resultado da subtração é Negativo")

if escolha == 3:
    multiplicação = primeiro_numero * segundo_numero
    if multiplicação % 2 == 0:
        print("O resultado da multiplicação é PAR")
    else:
        print("O resultado da subtração é Impar")
    if multiplicação == round(multiplicação):
        print("O resultado da multiplicação é Inteiro")
    else:
        print("O resultado da multiplicação é Decimal")
    if multiplicação > 0:
        print("O resultado da mutiplicação é Positivo")
    else:
        print(f"O resultado da multiplicação é Negativo")

if escolha == 4:
    divisão = primeiro_numero / segundo_numero
    if divisão % 2 == 0:
        print("O resultado da divisão é PAR")
    else:
        print("O resultado da divisão é Impar")
    if divisão == round(divisão):
        print("O resultado da divisão é Inteiro")
    else:
        print("O resultado da divisão é Decimal")
    if divisão > 0:
        print("O resultado da divisão é Positivo")
    else:
        print(f"O resultado da divisão é Negativo")