'''Faça um programa que peça 10 números inteiros.
No final, o programa deve calcular e mostrar:
A quantidade de números pares.
A quantidade de números ímpares.'''
impares = []
pares = []
for i in range(1, 11):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(f"Quantidade de Números PARES: {len(pares)}")
print(f"Quantidade de Números IMPARES: {len(impares)}")

#Outra forma de resolver o mesmo problema: (A forma abaixo economiza mais memória)

'''
impares = 0
pares = 0
for i in range(1, 11):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"Quantidade de Números PARES: {pares}")
print(f"Quantidade de Números IMPARES: {impares}")
'''