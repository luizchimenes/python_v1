print("ANÁLISE DE TRIÂNGULOS")
print(30*'-=-')
n1 = float(input("Primeiro segmento:"))
n2 = float(input("Segundo segmento: "))
n3 = float(input("Terceiro segmento:"))
print(30*'-=-')
if (n1 < n2 + n3) and (n2 < n1 + n3) and (n3 < n1 + n2):
    print('0s segmentos digitados PODEM FORMAR um Triângulo!')
else:
    print("Os segmentos digitados acima NÃO PODEM formar um Triângulo.")