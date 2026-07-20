'''Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a
função de potência da linguagem'''
resultado = 1
base = int(input("Digite o número BASE: "))
expoente = int(input("Digite o número EXPOENTE: "))
while expoente == 0:
    print("O expoente precisa ser diferente de ZERO")
    expoente = int(input("Digite o número EXPOENTE: "))

for i in range (expoente):
    resultado *= base

print(f"O resultado do número {base} elevado ao {expoente}: {resultado}")
