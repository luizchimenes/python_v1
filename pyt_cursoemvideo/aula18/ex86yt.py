# Digitar 7 valores e cadastrá-los em uma única lista que os separe em pares e ímpares em ordem crecente
lista = []
for c in range(7):
    num = int(input("Digite um valor inteiro: "))
    if num % 2 == 0:
        pares = []
        pares.append(num)
    if num % 2 == 1:
        impares = []
        impares.append(num)
    lista.append(pares)
lista.append(pares)
lista.append(impares)
pares.sort()
impares.sort()
print(f"O números pares foram {lista[0]}")
print(f"Os números ímpares foram {lista[1]}")