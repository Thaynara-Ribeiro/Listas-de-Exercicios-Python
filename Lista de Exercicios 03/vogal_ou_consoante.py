#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
print("---Sopa de Letrinhas---")
letra = input("Digite uma letra qualquer: ").upper()
if letra in "AEIOU":
    print("E uma Vogal")
else:
    print("E uma Consoante")
