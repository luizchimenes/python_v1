# Criar palpites para a Mega Sena - Pergunta quantos jogos serão gerados e sortea 6 números de 1 a 60
# Cadastra tudo em uma lista composta
# Não deu muito certo
from random import randint
lista = []
jogos= []
cont = 0
quest = int(input("Quantos jogos deseja? "))
tot = 1
while tot <= quest:
    while True:
        x = randint(1,60)
        if x not in lista:
            lista.append(x)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(jogos)