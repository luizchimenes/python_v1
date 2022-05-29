# Números primos
num = int(input("Digite um número: "))
cont = 0
for c in range(1, num + 1):
    if (num % c == 0):
        cont += 1
if (cont == 2):
    print("O número {} É PRIMO, pois só é divisivel por ele mesmo e 1.".format(num))
else:
    print("O número {} NÃO É PRIMO, pois é divísivel por {} números.".format(num,cont))