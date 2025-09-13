#7 Realiza a leitura de 1 int e apresenta se ele é par ou ímpar.
n = int(input('Digite um número: '))
if n % 2 == 0:
    print('O número {} é PAR'.format(n))
else:
    print('o número {} é IMPAR'.format(n))
