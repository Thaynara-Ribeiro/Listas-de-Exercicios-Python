'''Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a populaçãode
B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários
para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
Faça uma adptação permitindo que o usuário informe as populações e as taxas de crescimento iniciais. '''
anos = 0
primeiro_pais = int(input("Digite qual a quantidade de habitantes da 1ª população: "))
taxa_de_crescimento_primeira_populacao = float(input("Digite qual taxa de crescimento anual: "))
segundo_pais = int(input("Digite qual a quantidade de habitantes da 2ª população: "))
taxa_de_crescimento_segunda_populacao = float(input("Digite qual taxa de crescimento anual: "))
while True:
    #Converter taxas de porcentagem em fatores de multiplicação reais.
    primeiro_pais = primeiro_pais * (1 + (taxa_de_crescimento_primeira_populacao/100)) 
    segundo_pais = segundo_pais * (1 + (taxa_de_crescimento_segunda_populacao/100))
    anos = anos + 1
    if primeiro_pais >= segundo_pais:
        print(f"A população A ultrapassará ou igualará a população B em {anos} anos.")
        break