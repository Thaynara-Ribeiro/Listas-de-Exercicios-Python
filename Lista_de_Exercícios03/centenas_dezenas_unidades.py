'''Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16'''
numero = int(input("Digite um valor qualquer (Abaixo de 1000R$): "))
#Solicitação de uma entrada do usuário
if numero > 1000:
    print("Digite um número inferior a 1000R$")
#Validando a condição inicial do programa
else:
#Gerando as Centenas/Dezenas/Unidades
    centena = numero // 100
    dezena = (numero%100) // 10
    unidade = numero % 10
    partes = []
#Criando uma lista para incluir cada um dos elementos
    if centena > 0:
        if centena == 1:
            partes.append("1 centena")
        else:
            partes.append(f"{centena} centenas")
    if  dezena > 0:
        if dezena == 1:
            partes.append("1 dezena")
        else:
            partes.append(f"{dezena} dezenas")
    if unidade > 0:
        if unidade == 1:
            partes.append("1 unidade")
        else:
            partes.append(f"{unidade} unidades")
 #Retornando a partir da posição/comprimentos da lista quais as centenas/dezenas/unidades de um número       
    quantidade_de_elementos = len(partes)
    if quantidade_de_elementos == 3:
        print(f"{numero} = {partes[0]}, {partes[1]} e {partes[2]}")
    elif quantidade_de_elementos == 2:
        print(f"{numero} = {partes[0]} e {partes[1]}")
    elif quantidade_de_elementos == 1:
        print(f"{numero} = {partes[0]}")

