# Cálculo do fatorial
#from math import factorial
'''num = int(input("Digite o número que deseja o fatorial: "))
f = factorial(num)
print(f'O fatorial de {num} é {f}')'''
num = int(input('Digite o número: '))
c = num
f = 1
while c > 0:
    print('{}'.format(c),end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')





