#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida
data = input("Digite uma data para ser validada: ").split("/")
dia = int(data[0])
mes = int(data[1])
ano = int(data[2])
if ano <=0 or mes < 1 or mes > 12:
    print("Data Inválida")
else:
        dia_maximo = 31
        if mes in [4, 6, 9, 11]:
            dia_maximo = 30
        elif mes == 2:
            if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
                dia_maximo = 29
            else:
                dia_maximo = 28
            if dia > 0 and dia <= dia_maximo:
                print("Data Válida")
            else:
                print("Data Inválida")