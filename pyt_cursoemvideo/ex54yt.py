# Detector de Palíndromo(palavras ao contrario)
frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
'''for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''
if inverso == junto:
    print("TEMOS UM PALÍNDROMO!")
    print(inverso, junto)  
else:
    print("A frase digitada não é um palíndromo")
    print(junto, inverso)



