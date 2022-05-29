# Sequência de Fibonacci v1.0 - Ler um número N e mostre os N primeiros elementos de uma sequência
print('\033[34mSEQUÊNCIA DE FIBONACCI\033[m')
print(10*'-=-')
num = int(input('Quantos termos você deseja mostrar: '))
t1 = 0
t2 = 1
print(10*'-=-')
print(f'{t1} -> {t2}', end='')
cont = 3
while cont <= num:
     t3 = t1 + t2
     print(f' -> {t3}',end='')
     t1 = t2
     t2 = t3
     cont += 1
print(' -> FIM')
