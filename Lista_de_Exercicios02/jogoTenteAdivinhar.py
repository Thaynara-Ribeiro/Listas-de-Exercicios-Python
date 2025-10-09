#Escreva um programa que faça o computador "Pensar" em um número inteiro entre 0 até 10 para o usuário tentar descobrir
#qual foi o número escolhido pelo computador. O programa deve solicitar novos chutes até que o jogador acerte.
from random import randint

computador = randint(0, 10)
palpite = 0
chute = int(input('Usuário adivinhe qual número estou pensando de 0 até 10: '))
while chute != computador:
    chute = int(input('Usuário adivinhe qual número estou pensando de 0 até 5: '))
    palpite = palpite + 1
if chute == computador:
    print('PARABENS,você acertou eu pensei exatamente {}'.format(computador))
    print('O total de palpites necessários foi', palpite)

 