# Par ou Ímpar - Parar se o jog perder e mostrar o número de vitórias consecutivas
from random import randint
from time import sleep
vit = 0
while True:
    jog = int(input('Diga um valor: '))
    computador = randint(0,100)
    total = jog + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jog} e o computador {computador}. Total de {total}.', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Jogador \033[34mGANHOU\033[m')
            vit += 1
        else:
            print('Você \033[31mPERDEU\033[m')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você \033[34mGANHOU\033[m')
            vit += 1
        else:
            print('Você \033[31mPERDEU\033[m')
            break
    print('Vamos jogar novamente...')
    sleep(2)
print(f'FIM DE JOGO! Voce venceu {vit} vezes')

