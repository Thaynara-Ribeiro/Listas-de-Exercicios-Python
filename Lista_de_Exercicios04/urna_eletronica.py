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
candidatoA_votos = []
candidatoB_votos = []
votos_nulos = []

opção = int(input("Vote Aqui: "))
while opção != 0:
    if opção == 1:
        candidatoA_votos.append(opção)
    elif opção == 2:
        candidatoB_votos.append(opção)
    elif opção == 3:
        votos_nulos.append(opção)
    else:
        print("Digite um valor válido!")
    opção = int(input("Vote Aqui: "))

print("Votação Encerrada")
print(f"Quantidade contabilizada do Candidato A{len(candidatoA_votos)}")
print(f"Quantidade contabilizada do Candidato B{len(candidatoB_votos)}")
print(f"Quantidade contabilizada de Votos Nulos{len(votos_nulos)}")
total_de_votos = len(candidatoA_votos) + len(candidatoB_votos) + len(votos_nulos)
print(f"A soma total dos votos contabilizados: {total_de_votos}")
