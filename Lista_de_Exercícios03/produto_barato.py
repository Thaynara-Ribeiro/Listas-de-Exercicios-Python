'''Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre
pelo mais barato.'''
preços = []
for i in range(1,4):
    produtos = float(input(f"Digite o preços do {i}º preço: R$ "))
    preços.append(produtos)
menor_preço = min(preços)
preço_mais_barato = preços.index(menor_preço)+1
print(f"O produto mais barato e o {preço_mais_barato}º produto, custando {menor_preço:.2f}R$")
print("Você deve comprar este!")