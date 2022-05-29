from random import randint
from time import sleep
computador = randint(0,5) #Faz o comp. pensar
print("-=-"*20)
print("Estou pensando em um número entre 0 e 5. Consegue adivinhar?")
print("-=-"*20)
jog = int(input("Em que número eu pensei? "))
print("PROCESSANDO....")
sleep (4)
if jog == computador:
    print("Parabéns! Você me venceu!")
else:
    print(f"Você errou! Eu pensei no número {computador} e não no {jog}")
