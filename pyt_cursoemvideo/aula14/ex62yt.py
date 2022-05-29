# Progressao Aritmética v2.0 - Usando While
print('GERADOR DE P.A')
print(12*'-=-')
num = int(input("Digite o primeiro termo: "))
raz = int(input("Digite a razão da P.A: "))
cont = 0 
print(12*'-=-')
while cont < 10:
    print(f'{num}',end=' ')
    print('-> ' if cont < 9 else '-> FIM', end='')
    num += raz
    cont += 1

    