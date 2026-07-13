'''Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagemde
erro e voltando a pedir as informações.'''

while True:
    nome_usuario = input("Digite o seu nome de usuário: ").lower().strip()
    senha = input("Digite sua senha: ").lower().strip()
    if nome_usuario in senha:
#Utilizando o operador In podemos gerar um problema para nomes pequenos tipo "Ana" isso acontece por o nome está contido em determinadas palavras que podem ser usadas como senha.
#Podemos resolver retirando o In por uma igualdade ==   
        print("Sua senha não pode possuir seu nome de usuário.")
    else:
        print("Informações registradas em sistema. Obrigada por usar o programa")
        break
