# Interromper repetições While - break e continue
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma dos números digitados vale {s}')

