# Digitar vários números e cadastra-los em uma lista. Caso já esteja lá, não será adicionado
# Mostrar a lista com os números em ordem crescente
lista = []
soma = 0
while True:
    num = int(input("Digite um valor inteiro: "))
    if num not in lista:
        lista.append(num)
        print("Valor adicionada à lista")
        soma += 1
    else:
        print("Valor já existente")
    cont = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    if cont == 'N':
        break
print(20*'-=')
lista.sort()
print(f"Foram adicionados {soma} itens à lista!")
print(f"A lista é {lista}")