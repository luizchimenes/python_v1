# Maior e menor da sequência
maior = 0
menor = 0
for c in range(1,6):
    peso = float(input("Digite o peso da {}° pessoa ".format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('O MAIOR peso lidoo foi {}kg e o MENOR foi {}kg'.format(maior,menor))