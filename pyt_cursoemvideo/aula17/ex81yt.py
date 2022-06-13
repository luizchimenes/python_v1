# Ler 5 números e colocá-los em ordem sem usar .sort()
lista = []
for c in range(5):
    num = int(input("Digite um valor: "))
    if c == 0 or num > lista[len(lista) - 1]:
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1
print(20*'-=')
print(f"Os valores em ordem na lsita são {lista}")
