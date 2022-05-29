# Análise de Dados em uma Tupla - ler quatro valores e guarde-os numa tupla
# Quantos 9 apareceram/ Em que posição aparece o primeiro 3/ Quais foram os pares
tupla = (int(input('Digite o 1° número: ')),
int(input('Digite o 2° número: ')),
int(input('Digite o 3° número: ')),
int(input('Digite o 4° número: ')))
print(f'Você digitou os números: {tupla}')
print(f'O número 9 apareceu {tupla.count(9)} vezes!')
if 3 in tupla:
    print(f'O primeiro 3 apareceu na posição {tupla.index(3) + 2}')
else: 
    print('O valor 3 não foi digitado')
print('Os valores pares da tupla são: ')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
    
        

