import random # from random import choice
n1 = str(input("Digite o nome de um aluno: "))
n2 = str(input("Digite o nome de um aluno: "))
n3 = str(input("Digite o nome de um aluno: "))
n4 = str(input("Digite o nome de um aluno: "))
lista = [n1,n2,n3,n4]
escolhido = random.choice(lista)
print("O aluno escolhido foi {}".format(escolhido))