# Tupla com nomes de produtos e seus preços na sequência - mostrar uma listagem de preços
# organizando os dados em forma tabular
tupla = ('Caneta', 2.00,
'Borracha', 3.00,
'Lápis', 1.50,
'Caderno', 10.00,
'Mochila da Jordan', 169.90,
'Lapiseira Stabilo', 15.90,
'Livro de Português', 149.90)
print(12*'-=-')
print(f'{"LISTAGEM DE PREÇOS":^40}')
for item in range(0,len(tupla)):
    if item % 2 == 0:
        print(f'{tupla[item]:.<30}',end=' ')
    else:
        print(f'R${tupla[item]:>5.2f}')