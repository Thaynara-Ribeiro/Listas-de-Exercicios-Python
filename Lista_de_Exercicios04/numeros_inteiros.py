#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
primeiro_valor = int(input("Digite o 1º valor: "))
segundo_valor = int(input("Digite o 2º valor: "))

print(f"Esses sãos os números inteiros entre {primeiro_valor} e {segundo_valor}")
if primeiro_valor <= segundo_valor:
    for i in range (primeiro_valor, segundo_valor + 1):
        if i % 1 == 0:
            print(i, end=" ")
else:
    for i in range(primeiro_valor,segundo_valor -1,-1):
        print(i, end=" ")