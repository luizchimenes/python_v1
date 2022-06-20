# Criar palpites para a Mega Sena - Pergunta quantos jogos serão gerados e sortea 6 números de 1 a 60
# Cadastra tudo em uma lista composta
from random import randint
lista = []
lista_total= []
cont = 0
jogos = int(input("Quantos jogos deseja? "))
tot = 1
while tot <= jogos:
    while True:
        x = randint(1,60)
        if x not in lista:
            lista.append(x)
            cont += 1
        if cont == 6:
            break
    lista.sort()
    lista_total.append(lista[:])
    lista.clear()
    tot += 1
print(lista_total)