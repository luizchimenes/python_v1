# Estatísticas em produtos - ler nome e preço de vários produtos - perguntar se quer continuar
# Total gasto, quantos custam mais de R$ 1000 e qual é o nome do mais barato
total = totmil = menor = cont = 0
barato = ''
while True:
    name = str(input('Nome do Produto: ')).strip()
    price = float(input('Preço do Produto: R$ '))
    total += price
    cont += 1
    if price > 1000:
        totmil += 1
    if cont == 1:
        menor = price
        barato = name
    else:
        if price < menor:
            menor = price
            barato = name
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja CONTINUAR [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('\033[31mFIM DO PROGRAMA\033[m')
print(f'O Total da compra foi de R${total}')
print(f'{totmil} produtos custam mais de R$1000')
print(f'O produto mais barato foi {barato} que custa R${menor}')
