# Soma de impares múltiplos de três
soma = 0
cont = 0
for c in range(1,501,2):
    if (c % 3 == 0):
        soma += c
        cont += 1
print(f"{cont} números foram somados.", end='')
print(f"A soma dos valores solicitados é {soma}!")