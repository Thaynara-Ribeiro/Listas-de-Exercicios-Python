'''11 As Organizações Hamurabi Medeiros resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram
para desenvolver o programa que calculará os reajustes.
• Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no
salário atual:
• salários até R$ 280,00 (incluindo) : aumento de 20%
• salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
• salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
• salários de R$ 1500,00 em diante : aumento de 5%
• Após o aumento ser realizado, informe na tela:
• o salário antes do reajuste;
• o percentual de aumento aplicado;
• o valor do aumento;
• o novo salário, após o aumento.'''
salario = float(input('Digite seu salário atual: '))
if salario <= 250:
    percentualAumento = 20
elif salario > 250 and salario <= 700:
    percentualAumento = 15
elif salario > 700 and salario <= 1500:
    percentualAumento = 10
else:
    percentualAumento = 5
valorSalario = salario * (percentualAumento/100)
novoSalario = salario + valorSalario 
print('Salário antes do reajuste', salario)
print('Percentual de aumento aplicado', percentualAumento)
print('Valor do aumento', valorSalario)
print('Novo salário, após o aumento', novoSalario)  