import random
n1 = str(input("Aluno que irá apresentar: "))
n2 = str(input("Aluno que irá apresentar: "))
n3 = str(input("Aluno que irá apresentar: "))
n4 = str(input("Aluno que irá apresentar: "))
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print("A ordem de apresentação será")
print(lista)
