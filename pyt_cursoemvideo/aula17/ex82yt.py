#  Ler vários números e colocá-los em uma lista
# Mostrar: quantos foram digitados/ lista em ordem decrescente/ se o valor 5 foi digitado
lista = []
soma = 0
while True:
    num = int(input("Digite um valor inteiro: "))
    print("Valor adicionado com sucesso")
    lista.append(num)
    soma += 1
    quest = str(input("Deseja continuar? [S/N] ")).upper().strip()
    if quest == 'N':
        break
print(20*'-=')
print(f"A sua lista é \033[36m{lista}\033[m")
print(f"Foram digitados \033[35m{soma}\033[m valores!")
lista.sort(reverse = True)
print(f"A lista em ordem decrescente é \033[36m{lista}\033[m")
if 5 in lista:
    print("O valor 5 \033[34mESTÁ\033[m na lista")
elif 5 not in lista:
    print("O valor 5 \033[31mNÃO\033[m está na lista")
print(f"-=- FIM DO PROGRAMA -=-")
