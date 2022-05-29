# Analisador Completo
soma_idades = 0
maior_idade_homem = 0
nome_mais_velho = ''
totmulher20 = 0
for p in range(1,5):
    print('----- {}° PESSOA -----'.format(p))
    nome = str(input("NOME: ")).strip()
    idade = int(input("IDADE: "))
    sexo = str(input("SEXO[M/F]: ")).strip()
    soma_idades += idade
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Mn' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
media_idades = soma_idades/4
print('A média de idade do grupo é de {} anos! '.format(media_idades))
print('O homem mais velho é {}, que possui {} anos'.format(nome_mais_velho,maior_idade_homem))
print("O total de mulheres com menos de 20 anos é {}".format(totmulher20))