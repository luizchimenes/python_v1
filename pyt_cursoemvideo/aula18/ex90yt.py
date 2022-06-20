# Ler nome e duas notas de vários alunos e guardá-los em uma lista composta
# Mostrar o boletim contendo a média e as notas de cada aluno individualmente
from time import sleep
ficha =[]
while True:
    nome = str(input("Nome: ")).strip()
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2)/ 2
    ficha.append([nome, [nota1, nota2], media])
    quest = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
    if quest == "N":
        break
print(20*'-=-')
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    option = int(input("De qual aluno deseja ver as notas? [999 interrompe] "))
    if option == 999:
        print("Finalizando")
        sleep(2)
        break
    if option <= (len(ficha) - 1):
        print(f"Notas de {ficha[option][0]} são: [{ficha[option][1]}]")
print("-=-= FIM DO PROGRAMA -=-=")
