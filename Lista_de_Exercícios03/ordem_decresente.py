#Faça um Programa que leia três números e mostre-os em ordem decrescente
lista_de_numeros = []
for i in range(1,4):
    numero = int(input("Digite um número qualquer: "))
    lista_de_numeros.append(numero)
lista_de_numeros.sort(reverse=True)
print(f"Números em ordem decresente= {lista_de_numeros}")
