# Aula de Listas (Parte 1 ) - Mundo 3
valor = []
'''valor.append(5)
valor.append(8)
valor.append(6)'''
for c in range(4):
    valor.append(int(input('Digite um valor: ')))
#for v in valor:
    #print(v, end='...')
for c, v in enumerate(valor):
    print(f'Na posição {c} encontrei {v}')
print(f'{"FIM":^30}')