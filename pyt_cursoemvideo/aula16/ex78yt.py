# Tupla com várias palavras - mostrar quais as vogais de cada uma
tupla = ('ARARA', 'TUPLA', 'JERIQUAQUARA', 'CURITIBA', 'APITO', 'CORONA', 'PARALELEIPIPEDO', 'UREIA')
for p in tupla:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra in 'AEIOU':
            print(letra, end=' ')
