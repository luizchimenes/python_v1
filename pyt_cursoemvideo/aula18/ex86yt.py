# Digitar 7 valores e cadastrá-los em uma única lista que os separe em pares e ímpares em ordem crecente
lista = [[], []]
for c in range(7):
    num = int(input("Digite um valor inteiro: "))
    if num % 2 == 0:
        lista[0].append(num)
    elif num % 2 == 1:
        lista[1].append(num)
print(20*"-=")
lista[0].sort()
lista[1].sort()
print(f"Os números pares foram : {lista[0]}")
print(f"Os números ímpares foram: {lista[1]}")
    