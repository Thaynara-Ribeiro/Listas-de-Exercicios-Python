#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F -Feminino, M -Masculino, Sexo Inválido.
sexo = input("Digite seu sexo (F ou M): ").upper()
if sexo == "F":
    print("Sexo FEMININO")
elif sexo == "M":
    print("Sexo MASCULINO")
else:
    print("Sexo Inválido")