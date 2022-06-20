# Melhorar o desafio anterior : mostrar a soma dos valores pares
# a soma dos valores da terceira coluna e o maior valor da segunda linha
matriz = []
soma_total = 0
soma_terceira = 0
maior = 0
for i in range(3):
    matriz.append([])
    for j in range(3):
        matriz[i].append(int(input(f"Digite o número da posição [{i}x{j}]: ")))
        soma_total += matriz[i][j]
        if j == 2:
            soma_terceira += matriz[i][j]
        if i == 1 and j == 0:
            maior = matriz[i][j]
        if i == 1 and j != 0:
            if matriz[i][j] > maior:
                matriz[i][j] = maior
print(10*'=-=')
for i in range(3):
    for j in range(3):
        print(f"[{matriz[i][j]}]", end='')
    print()