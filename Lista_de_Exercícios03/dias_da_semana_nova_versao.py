'''Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2-Segunda, etc.), se digitar outro valor deve
aparecer valor inválido.'''
print("---Dias da Semana---")
dias_da_semana = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabado"]
dia = int(input("Digite o número correspondente (1-Domingo, 2-Segunda...): "))
if dia >= 1 and dia <=7:
    dia_escolhido = dias_da_semana[dia-1]
    print(f"Dia da Semana = {dia_escolhido}")
else:
    print("Valor Inválido")