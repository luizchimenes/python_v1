# Menu de Opções - Ler dois valores e realizar as funções apresentadas
from time import sleep
n1 = int(input("Digite o 1° número: "))
n2 = int(input("Digite o 2° número: "))
n = 0
while n != 5:
    n = int(input('''>>>O QUÊ DESEJA:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA: '''))
    print(15*'==')
    if n == 1:
        soma = n1 + n2
        print(f"{n1} + {n2} = {soma}")
        print(15*'==')
    elif n == 2:
        mult = n1*n2
        print(f'{n1} x {n2} = {mult}') 
        print(15*'==')
    elif n == 3:
        if n1 > n2:
            print(f'{n1} é o MAIOR!')
        else:
            print(f'{n2} é o MAIOR')
    elif n == 4:
        print('Informe os números novamente')
        n1 = int(input('Digite o 1° número: '))
        n2 = int(input("Digite o 2° número: "))
    elif n == 5:
        print('Finalizando...')
        sleep(2)
        print(15*'==')
    else: 
        print("Número inválido")
print('FIM')