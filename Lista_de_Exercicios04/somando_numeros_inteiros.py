'''Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles
Altere o programa anterior para mostrar no final a soma dos números'''
soma = 0
primeiro_valor = int(input("Digite o 1º valor: "))
segundo_valor = int(input("Digite o 2º valor: "))

print(f"Esses sãos os números inteiros dentro do intervalo informado ({primeiro_valor}/{segundo_valor})")
if primeiro_valor <= segundo_valor:
    for i in range (primeiro_valor, segundo_valor + 1):
            soma += i
            print(i, end=" ")
else:
    for i in range(primeiro_valor,segundo_valor -1,-1):
        soma += i
        print(i, end=" ")

print(f"A soma dos números: {soma}")