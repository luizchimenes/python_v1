# Simulador de Caixa Eletrônico - Perguntar o valor que quer sacar
# Informar quantas cèdulas de calar valor serão entregues ( 50, 20, 10 e 1)
# Última do Mundo 2 - Curso em vídeo
print('\033[34mBANCO LUIZIN\033[m')
valor = int(input('Digite o valor que deseja sacar: R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break

