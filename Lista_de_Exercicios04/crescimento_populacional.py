'''Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a populaçãode
B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários
para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.'''
anos = 0
primeiro_pais = 80000
segundo_pais = 200000
while True:
    primeiro_pais = primeiro_pais * 1.03
    segundo_pais = segundo_pais * 1.015
    anos = anos + 1
    if primeiro_pais >= segundo_pais:
        print(f"A população A ultrapassará ou igualará a população B em {anos} anos.")
        break