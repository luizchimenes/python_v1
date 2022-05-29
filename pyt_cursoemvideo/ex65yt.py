# Tratando vários valores v1.0 - Ler vários números / só para quando n = 999 / mostras quantos foram e a soma deles
print('\033[34mTRATANDO VALORES\033[m')
print(10*'-=-')
soma = 0
total = 0
num = 0
num = int(input('Digite um valor: '))
while num != 999:
    total += 1
    soma += num
    num = int(input('Digite um valor: '))
print(f'Foram digitados {total} números e a soma deles é {soma}')

