# Declarar uma matriz 3 x 3 e preencher ela com valores lidos
# Mostrar a matriz na tela, com a formatação correta
matriz = []
for i in range(3):
    matriz.append([])
    for j in range(3):
        matriz[i].append(int(input(f"Digite o número da posição [{i}x{j}]: ")))
print(15*'=-=')
for i in range(3):
    for j in range(3):
        print(f"[{matriz[i][j]:^5}]", end='')
    print()

        