#Faça um programa que leia 5 números e informe o maior número.
lista = []
for i in range (1, 6):
    numero = int(input("Digite um número: "))
    lista.append(numero)
maior_numero = max(lista)
print(f"O maior número: {maior_numero}")
