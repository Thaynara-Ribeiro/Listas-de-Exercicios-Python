n1 = float(input('Digite o primeiro número: '))
n2 = float('Digite o segundo número:')
soma = n1 + n2
sub = n1 - n2
mult =  n1 * n2
div = n1  /n2
resto = n1 % n2
escolha = int (input('Escolha uma opção: \n[1] Soma\n[2] Subtração\n [3] Multiplicação\n[4] Divisão\n[5] Resto da Divisão\n'))
if escolha == 1:
    print('A soma dos números {} e {} é {}'.format(n1,n2,soma))
elif escolha == 2:
    print('A subtração dos números {} e {} é {}'.format(n1,n2,sub))
elif escolha == 3:
    print('A Multiplicação dos números {} e {} é {}'.format(n1,n2,mult))
elif escolha == 4:
    print('A Divisão dos números {} e {} é {}'.format(n1,n2,div))
elif escolha == 5:
    print('O Resto da Divisão dos números {} e {} é {}'.format(n1,n2,resto))
else:
    print('Opção inválida, tente novamente!')

