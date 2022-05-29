# Tuplas com times de Futebol - 20 primeiros colocados do campeonato ( SÉRIE B 2022)
# Mostrar: 5 primeiros/ 4 últimos/ Em ordem alfabética/ Posição da Chape
times = ('Cruzeiro', 'Bahia', 'Sport', 'Vasco', 'Novorizontino', 'Grêmio', 'Operário,'
'Brusque', 'Criciúma', 'Chapecoense', 'Ituano', 'Sampaio Corrêia', 'Ponte Preta', 'Náutico',
'Londrina', 'Vila Nova', 'CSA', 'Guarani', 'CRB', 'Tombense')
print(12*'-=-')
print(f'A tabela atual da Série B 2022 é : {times}')
print(12*'-=-')
print(f'Os 5 primeiros são: {times[0:5]}')
print(12*'-=-')
print(f'Os 4 últimos são:  {times[15:20]}') # ou times[-4:]
print(12*'-=-')
print(f'Em ordem alfabética: {sorted(times)}')
print(12*'-=-')
print(f'A Chapecoense está em {times.index("Chapecoense") + 2}º lugar')
print(12*'-=-')
print('FIM DO PROGRAMA')
