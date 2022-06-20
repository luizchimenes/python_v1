# Melhorar o desafio anterior : mostrar a soma dos valores pares
# a soma dos valores da terceira coluna e o maior valor da segunda linha
matriz = []
soma_pares = 0
soma_terceira = 0
maior = 0
for i in range(3):
    matriz.append([])
    for j in range(3):
        matriz[i].append(int(input(f"Digite o número da posição [{i}x{j}]: ")))
print(10*'=-=')
for i in range(3):
    for j in range(3):
        print(f"[{matriz[i][j]}]", end='')
        if matriz[i][j] % 2 == 0:
            soma_pares += matriz[i][j]
    print()
print(15*'-=-')
print(f"A soma de todos os números pares vale {soma_pares}!")
for i in range(3):
    soma_terceira = matriz[i][2]
print(f"A soma dos números da terceira coluna vale {soma_terceira}!")
for j in range(3):
    if j == 0:
        maior = matriz[1][j]
    elif matriz[1][j] > maior:
        maior = matriz[1][j]
print(f"O maior número da segunda linha é {maior}!")
