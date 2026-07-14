'''Faça um programa que leia e valide as seguintes informações:
• Nome: maior que 3 caracteres;
• Idade: entre 0 e 150;
• Salário: maior que zero;
• Sexo: 'f' ou 'm';
• Estado Civil: 's', 'c', 'v', 'd’;'''

while True:
    nome = input("Digite o seu nome: ").strip()
    if len(nome) <= 3:
        print("O nome precisa possuir no minimo quatro caracteres")
    else:
        print(f"Nome: {nome} cadastrado!")
        break
while True:
    idade = int(input("Digite sua idade: "))
    if idade < 0 or idade > 150:
        print("Digite uma idade entre 0 até 150 anos.")
    else:
        print(f"Idade: {idade} cadastrada!")
        break
while True:
    salario = float(input("Digite seu salário: "))
    if salario <= 0:
        print("Digite um salário Válido!")
    else:
        print(f"Salário: {salario:.2f} cadastrado!")
        break
while True:
    sexo = input("Digite seu sexo (F ou M): ").lower()
    if sexo not in ["f", "m"]:
        print("Digite um sexo Válido (F ou M)")
    else:
        if sexo == "f":
            print("Sexo Feminino Cadastrado com Sucesso")
            break
        else:
            print("Sexo Masculino Cadastrado com Sucesso")
            break
while True:
    estado_civil = input("Digite o seu estado civil atual (S,C,V,D): ").lower()
    if estado_civil not in ["s","c","v","d"]:
        print("Digite um estado civil Válido! (S,C,V,D): ")
    else:
        print("Estado Civil Cadastrado com Sucesso")
        break
