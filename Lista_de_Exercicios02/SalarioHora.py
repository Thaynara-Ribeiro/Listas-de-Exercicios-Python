#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#• Calcule e mostre o total do seu salário no referido mês
valor_hora = float(input('Quanto você ganha no mês? R$ '))
horas_trabalhadas = float(input('Quantas horas você trabalha no mês? '))
salario = valor_hora * horas_trabalhadas
print('Baseado nas informações fornecidas, seu salário no mês é',round(salario,2))