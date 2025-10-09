#Faça um programa que leia o sexo de uma pessoa, mas só aceite F ou M. Caso seja digitado algo diferente solicite a
#entrada dos dados novamente.
sexo = input('Digite seu sexo (F/M): ').upper()
while sexo != 'F' and sexo != 'M':
    sexo = input('Digite seu sexo (F/M): ').upper()
print('Sexo cadastrado com sucesso!')