# Vários números com flag - Soma e quantos - 999 para
soma  = cont = 0
num = 0
while True:
    num = int(input('Digite um número(999 para parar): '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'Foram digitados {cont} números e a soma deles vale {soma}')