#Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão)
print("---Par ou Impar---")
numero = int(input("Digite um número para saber se ele é PAR ou IMPAR: "))
if numero % 2 == 0:
    print("PAR")
else:
    print("IMPAR")