# Aula sobre listas compostas
lista = []
x = 0
while True:
    lista.append([])
    nome = str(input("Digite seu nome: ")).strip()
    lista[x].append(nome)
    idade = int(input("Digite sua idade: "))
    lista[x].append(idade)
    x += 1
    quest = str(input("Deseja continuar? [S/N] ")).upper().strip()
    if quest == "N":
        break
print(lista)
for p in lista:
    print(f"{p[0]} tem {p[1]} anos de idade!")
    

