# Soma dos Pares
soma = 0
cont = 0
for n in range(6):
    num = int(input("Digite um número inteiro: "))
    if (num % 2 == 0):
        soma += num
        cont += 1
print(f"{cont} números PARES foram digitados!",end=' ')
print(f"A SOMA desses números é {soma}.")
    