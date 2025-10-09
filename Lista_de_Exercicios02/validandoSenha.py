#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
#mostrando uma mensagemde erro e voltando a pedir as informações

nomeDeUsario = input('Digite seu nome de usuário: ')
senha = input('Digite sua senha: ')
while True:
    if nomeDeUsario == senha:
        print('Não é possivel inserir uma senha igual ao nome do seu usuario')
        nomeDeUsario = input('Digite seu nome de usuário: ')
        senha = input('Digite sua senha: ')
    else:
        print('Cadastro confirmado com sucesso!')
        break

