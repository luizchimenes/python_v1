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
for l in range(3):
    
