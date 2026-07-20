#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores
numeros = []
while True:
    numero = int(input("Insira um número [Digite 0 para SAIR]: "))
    if numero == 0:
        break
    numeros.append(numero)    
if len(numeros) > 0:
    print(f"O maior número inserido foi: {max(numeros)}")
    print(f"O menor número inserido foi: {min(numeros)}")
    print(f"A soma dos números {sum(numeros)}")
else:
    print("Nenhum número foi inserido!")
print("Obrigada por usar o aplicativo.")





