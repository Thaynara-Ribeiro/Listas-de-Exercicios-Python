#Escreva um código que represente um Menu Interativo de uma locadora, possuindo as seguintes opções:
#(Listar, Adicionar, Quantidade de filmes adicionados, Sair)


filmes = []
while True:
    print('---- Locadora de Filmes ----')
    print('\n1) Listar \n2) Adicionar \n3) Quantidade \n4) Sair')
    escolha = int(input('Digite sua opção: '))
    if escolha  == 1:
        if len(filmes) == 0:
            print('Não existem filmes a serem exibidos')
        else:
            print('---- Filmes já adicionados ----')
            for itens in filmes:
                print('-',itens)
    elif escolha == 2:
        novoFilme = input('Digite o nome do filme: ')
        filmes.append(novoFilme)
        print('Filme inserido com sucesso!')
    elif escolha == 3:
        if len(filmes) == 0:
            print('Atualmente não possuimos nenhum filmes adicionados')
        else:
            print('Atualmente temos',len(filmes), 'filmes adicionados')
    elif escolha == 4:
        print('Obrigada por utilizar os nossos serviços online\nAté uma proxima')
        break
    else:
        print('Opção Invalida')