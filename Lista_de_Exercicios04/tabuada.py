'''Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual
numero ele deseja ver a tabuada.'''
numero = int(input("Digite um número (1 até 10) para mostrar sua TABUADA: "))
while numero < 1 or numero > 10:
    print("Digite um número válido - Programa atual possui Tabuada apenas (1 até 10)")
    numero = int(input("Digite um número (1 até 10) para mostrar sua TABUADA: "))
print(f"Tabuada de {numero}")
for i in range (1, 11):
    mutiplicador = numero * i
    print(f"{numero} X {i} = {mutiplicador}")
