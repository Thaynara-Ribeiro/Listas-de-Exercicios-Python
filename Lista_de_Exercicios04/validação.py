'''Mostre uma mensagem de erro caso o valor seja inválido (por exemplo, se o usuário digitar 12 ou -3) e continue pedindo a 
nota até que o usuário informe um valor válido. Quando ele finalmente digitar uma nota correta 
(ex: 7.5), o programa deve exibir: "Nota salva com sucesso!"'''
while True:
    nota = float(input("Digite uma nota (0 até 10): "))
    if nota < 0 or nota > 10:
        print("Nota Inválida!")
    else:
        print("Nota salva com sucesso!")
        break

#Outra forma de resolver o mesmo problema:

'''
nota = float(input("Digite uma nota (0 até 10): "))
while nota < 0 or nota > 10:
    print("Nota Inválida!")
    nota = float(input("Digite uma nota (0 até 10): "))
print("Nota salva com sucesso!")
'''