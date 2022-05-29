# Análise de dados do grupo - Cadastrar pessoas, perguntar se quer continuar
# Pessoas com + de 18, Quantos homens e quantas mulheres com - de 20 anos
dezoito = homens = mulvinte = total = 0
while True:
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    idade = int(input('Digite sua idade: '))
    total += 1
    continuar = ' '
    if sexo == 'M':
        homens += 1
    if idade >= 18:
        dezoito += 1
    if (sexo == 'F') and (idade < 20):
        mulvinte += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print('FIM DO PROGRAMA')
print(f'{dezoito} pessoas possuem mais de 18 anos')
print(f'{homens} de {total} pessoas são homens')
print(f'{mulvinte} mulheres possuem menos de 20 anos')
