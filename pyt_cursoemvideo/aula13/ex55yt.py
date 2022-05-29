# Grupo da Maioridade
maior = 0
menor = 0
for c in range(1,8):
    age = int(input("Digite a idade da {}° pessoa ".format(c)))
    if age >= 18:
        maior += 1
    else:
        menor += 1
print("{} pessoas atingiram a maior idade e {} ainda são de menor!".format(maior,menor))