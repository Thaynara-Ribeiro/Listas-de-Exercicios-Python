'''Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de
cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de
1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma notade
5 e quatro notas de 1.'''
print("===Caixa Eletrônico===")
print('''Notas disponiveis
100,00R$
50,00R$
10R$
5R$
1R$
Valor Minimo = 10R$
Valor Maximo = 600R$
''')
saque = int(input("Digite qual o valor do seu saque: "))

if saque < 10:
    print("Valor Minimo de Saque 10,00R$")
elif saque > 600:
    print("Valor Maximo de Saque 600,00R$")
else:
    notas_100 = saque // 100
    saque = saque % 100
    notas_50 = saque // 50
    saque = saque % 50
    notas_10 = saque // 10
    saque = saque % 10
    notas_5 = saque // 5  
    saque = saque % 5
    notas_1 = saque
    partes = []
    if notas_100 > 0:
        if notas_100 == 1:
            partes.append("uma nota de 100")
        else:
            partes.append(f"{notas_100} notas de 100")
    if notas_50 > 0:
        if notas_50 == 1:
            partes.append("uma nota de 50")
        else: 
          partes.append(f"{notas_50} notas de 50")
    if notas_10 > 0:
        if notas_10 == 1:
            partes.append("uma nota de 10")
        else:
            partes.append(f"{notas_10} notas de 10")
    if notas_5 > 0:
        if notas_5 == 1:
            partes.append("uma nota de 5")
        else:
            partes.append(f"{notas_5} notas de 5")
    if notas_1 > 0:
        if notas_1 == 1:    
            partes.append("uma nota de 1")
        else:
            partes.append(f"{notas_1} notas de 1")
    if len(partes) > 1:
        inicio = ", ".join(partes[:-1])
        fim = partes[-1]
        print(f"Para realizar o saque, o programa fornece {inicio} e {fim}.")
    elif len(partes) == 1:
        print(f"Para realizar o saque, o programa fornece {partes[0]}.")