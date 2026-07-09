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
resultado = 0
operação_valida = True
if escolha == 1:
    resultado = primeiro_numero + segundo_numero
elif escolha == 2:
    resultado = primeiro_numero - segundo_numero
elif escolha == 3:
    resultado = primeiro_numero * segundo_numero
elif escolha == 4:
    if segundo_numero != 0:
        resultado = primeiro_numero / segundo_numero
    else:
        print("ERRO - Não é possivel dividir por zero.")
        operação_valida = False
else:
    print("Opção Inválida")
    operação_valida = False

if operação_valida:
    print(f"O resultado da operação é: {resultado}")

    if resultado == round(resultado):
        if resultado % 2 == 0:
            print("E um número PAR")
        else:
            print("E um número IMPAR")
        print("E um número INTEIRO")
    else:
        print("E um número DECIMAL (Não é PAR nem IMPAR)")
    if resultado > 0 :
        print("E um número POSITIVO")
    elif resultado < 0:
        print("E um número NEGATIVO")
    else:
        print("E um número NEUTRO (Zero)")