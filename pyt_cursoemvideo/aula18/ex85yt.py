# ler nome e peso de várias pessoas guardando em listas
# Mostrar: quantas foram cadastradas, listas as mais pesadas e as mais leves
lista = []
temp = []
x= 0
maior = menor = 0
while True:
    temp.append(str(input("Nome: ")).strip())
    temp.append(int(input("Peso: ")))
    if len(lista) == 0:
        maior = menor = temp[1]
    else: 
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    lista.append(temp[:])
    temp.clear()
    question = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
    if question == "N":
        break
print(20*"-=-")
print(f"Foram cadastradas {len(lista)} pessoas")
print(f"O maior peso foi de {maior} de ", end='')
for p in lista:
    if p[1] == maior:
        print(p[0])
print(f"O menor peso foi de {menor} de ", end="")
for p in lista:
    if p[1] == menor:
        print(p[0])




    

