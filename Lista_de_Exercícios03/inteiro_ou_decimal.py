#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento
print("---Inteiro ou Decimal---")
numero = float(input("Digite um número qualquer: "))
if numero == round(numero):
    print("Inteiro")
else:
    print("Decimal")


'''
O Norte da Lógica Matemática
Pense comigo: se um número decimal muda de valor quando é arredondado, mas um número inteiro continua valendo a mesma coisa... como podemos usar isso em um if?
Nós podemos comparar o número original com a versão arredondada dele!
Imagine que o usuário digitou o número:
Caso 1: O usuário digita 15 (Inteiro)
O número original é 15.
Quanto é round(15)? É 15.
Pergunta: O número original (15) é igual ao número arredondado (15)? Sim! Então ele é Inteiro.
Caso 2: O usuário digita 15.3 (Decimal)
O número original é 15.3.
Quanto é round(15.3)? Ele arredonda para 15.
Pergunta: O número original (15.3) é igual ao número arredondado (15)? Não! Eles ficaram diferentes. Então ele é Decimal.
'''