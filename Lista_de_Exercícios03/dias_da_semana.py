'''Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2-Segunda, etc.), se digitar outro valor deve
aparecer valor inválido.'''
print("---Dias da Semana---")
dia = int(input("Digite o número correspondente (1-Domingo, 2-Segunda...): "))
if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda")
elif dia == 3:
    print("Terça")
elif dia == 4:
    print("Quarta")
elif dia == 5:
    print("Quinta")
elif dia == 6:
    print("Sexta")
elif dia == 7:
    print("Sabado")
else:
    print("Valor Inválido")

