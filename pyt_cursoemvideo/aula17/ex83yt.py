# Ler vários números e colocar em uma lista / Criar duas listas PARES e ÍMPARES 
# com os valores digitados / No final mostrar as três listas
total = []
pares = []
impares = []
while True:
    num = int(input("Digite um valor: "))
    total.append(num)
    if num % 2 == 0:
        pares.append(num)
    elif num % 2 == 1:
        impares.append(num)
    question = str(input("Deseja continuar? [S/N]: ")).strip().upper()
    if "N" in question:
        break
total.sort()
pares.sort()
impares.sort()
print(f"A lista total é {total}")
print(f"A lista de valores pares é {pares}")
print(f"A lista de valores ímpares é {impares}")
print("-=- FIM DO PROGRAMA -=-")