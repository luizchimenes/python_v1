# Número por extenso - zero até vinte - mostrar o número por extenso
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze',
  'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 a 20: '))
    if 0 <= num <= 20:
        print(f'{num} em extenso é {cont[num]}')
        option = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
        if option == 'N':
            break
        else:
            continue
    print('Número inválido! ', end='')
print(12*'-=-')
print('FIM DO PROGRAMA')
    

