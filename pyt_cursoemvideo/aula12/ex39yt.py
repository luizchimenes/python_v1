# Comparando números
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o segundo número: "))
print(30*'-=-')
if (n1 > n2) and (n1 > n3):
    print("O PRIMEIRO valor é o maior!")
elif (n2 > n1) and (n2 > n3):
    print('O SEGUNDO valor é o maior!')
elif (n1 == n2) and (n1 == n3):
    print("Os três valores são IGUAIS!")
elif( n1 == n2) and (n1 != n3):
    print("DOIS dos valores são iguais")
else:
    print("O TERCEIRO número é o maior!")
