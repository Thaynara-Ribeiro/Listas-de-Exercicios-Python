'''Desenvolva um programa que simule uma urna eletrônica simples.
O programa deve ler os votos de vários eleitores. Para cada eleitor, ele deve pedir um voto (um número inteiro).
Use as seguintes opções:
1 - Candidato A
2 - Candidato B
3 - Voto Nulo
0 - Encerrar a votação
Quando o usuário digitar 0, o programa deve parar de pedir votos e mostrar na tela:
O total de votos do Candidato A.
O total de votos do Candidato B.
O total de votos nulos.
O total geral de votos computados (sem contar o zero).'''

print('''Urna Eletrônica
[1] Candidato A
[2] Canditato B
[3] Voto Nulo
[0] Encerrar Votação''')

votos_A = 0
votos_B = 0
nulos = 0 
opcao = int(input("Vote Aqui: "))
while opcao !=0:
    if opcao == 1:
        votos_A += 1
    elif opcao == 2:
        votos_B += 1
    elif opcao == 3:
        nulos += 1
    else:
        print("Digite uma opção válida!")
    opcao = int(input("Vote Aqui: "))

soma_de_votos = votos_A + votos_B + nulos
print("Votação Encerrada")
print(f"A soma de votos do Candidato A: {votos_A}")
print(f"A soma de votos do Candidato B: {votos_B}")
print(f"A soma dos votoso nulos: {nulos}")
print(f"Total de votos: {soma_de_votos}")