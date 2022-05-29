# Super Progressão Aritmética v3.0 - Termos a mais
print("\033[34mSUPER PROGRESSÃO ARITMÉTICA\033[m")
print(10*'-=-')
primeiro = int(input("Insira o primeiro termo da P.A: "))
raz = int(input("Insira a razão da P.A: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += raz
        cont += 1
    print('PAUSA')
    mais = int(input('Deseja mais termos? Se sim, quantos: '))
print(f'Progressao FINALIZADA! Foram {total} termos no total')
print('FIM')