# Jogo da adivinhação V2.0 - Adivinhar o número que o PC pensou - Usando While
from random import randint
computador = randint(0,10)
acertou = False
palp = 0
while not acertou:
    jogador = int(input("Qual é o número que eu eu pensei: "))
    palp += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente outra vez')
        else:
            print('Menos..')
print("Você ACERTOU em {} tentativas. O número escolhido foi {}".format(palp,computador))