# PEDRA, PAPEL E TESOURA
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
option = int(input("Qual sua opção? "))
print("JO",)
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print(15*'-=-')
print("Computador jogou {}".format(itens[computador]))
print("Jogador jogou {}".format(itens[option]))
print(15*'-=-')
if computador == 0:
    if option == 0:
        print("EMPATE")
    elif option == 1:
        print("JOGADOR GANHOU!")

    elif option == 2:
        print("O COMPUTADOR GANHOU")

    else:
        print("JOGADA INVÁLIDA")

elif computador == 1:
    if option == 0:
        print("O COMPUTADOR VENCEU")

    elif option == 1:
        print("EMPATE")
    elif option == 2:
        print("O JOGADOR VENCEU")
    else:
        print("JOGADA INVÁLIDA")

elif computador == 2:
    if option == 0:
        print("O JOGADOR VENCEU")

    elif option == 1:
        print("O COMPUTADOR VENCEU")
    elif option == 2:
        print("EMPATE")
    else:
        print("JOGADA INVÁLIDA")
