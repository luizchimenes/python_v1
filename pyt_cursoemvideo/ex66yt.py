# Maior e menor valores - Média dos valores e qual foi o maior e o menor valores
# Perguntar se quer continuar ou não
question = 'S'
soma = 0
cont = 0
media = 0
maior = 0
menor = 0
while question == 'S':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    question = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
media = soma/cont
print(f'A média dos valores é {media} de {cont} números digitados')
print(f'O MAIOR número é {maior} e o MENOR número é {menor}!')




