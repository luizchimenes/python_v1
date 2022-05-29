# ANALISANDO TRIÂNFULO v2.0
n1 = int(input("Digite a medida do preimeiro lado: "))
n2 =int(input("Digite a medida do segundo lado: "))
n3 = int(input("Digite a medida do terceiro lado: "))
if (n1 < n2 + n3) and (n2 < n1 + n3) and (n3 < n1 + n2):
    print('0s segmentos digitados PODEM FORMAR um Triângulo!')
    if (n1 == n2 == n3):
        print("O triângulo é EQUILÁTERO!")
    elif ((n1 == n2) and (n1 != n3)) or ((n1 == n3) and (n1 != n2)) or ((n2 == n3) and (n2 != n1)):
        print("0 triângulo é ISÓSCELES!")
    elif( n1 != n2 != n3):
        print("O triângulo é ESCALENO!")
else:
    print("Os segmentos NÃO FORMAM um triângulo.")