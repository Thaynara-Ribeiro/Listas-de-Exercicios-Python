#5 Realiza a leitura de 1 float referente ao valor de um produto e imprime o valor com descontos de 10%, 20% e 50%
p = float(input('Diigite o valor do produto: '))
print('O valor do produto com 10% de desconto é {:.1f}R$'.format(p * 0.9))
print('O valor do produto com 20% de desconto é {:.1f}R$'.format(p * 0.8))
print('O valor do produto com 50% de desconto é {:.1f}R$'.format(p * 0.5))