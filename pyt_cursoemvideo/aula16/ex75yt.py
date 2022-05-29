# Maior e Menor valores em Tupla - 5 números aleatórios e colocar em tupla
# Indicar o maior e o menor
from random import randint
num = (randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100))
print('Os valores sorteados são: ', end='')
for n in num:
    print(f'{n}',end=' ')
print(f'\nO maior número é {max(num)},')
print(f'E o menor número é {min(num)}!')

