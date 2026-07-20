#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
fatorial = 1
numero = int(input("Digite um número para calcular o seu FATORIAL: "))
for i in range (1, numero + 1):
    fatorial = fatorial * i

print(f"O fatorial {numero}! = {fatorial}")