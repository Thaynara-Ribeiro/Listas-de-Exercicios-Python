'''Faça um programa que leia a nota de 5 alunos.Para cada aluno, valide a nota com um while: ela precisa estar 
obrigatoriamente entre 0.0 e 10.0. No final, mostre:A média geral da turma (soma das notas / 5).Quantos alunos foram 
aprovados maior ou igual 7.0).'''
aprovados = []
notas = []

for i in range (1, 6):
    nota = float(input(f"Digite sua {i}ª nota: "))
    while nota < 0 or nota > 10:
        print("Nota inválida! A nota precisa está entre 0 até 10.")
        nota = float(input(f"Digite sua {i}ª nota: "))
    notas.append(nota)
    if nota >= 7:
        aprovados.append(nota)
print("---RESULTADO DA TURMA---")
print(f"A media geral: {sum(notas)/5:.2f}")
print(f"Quantidade de alunos aprovados {len(aprovados)}")