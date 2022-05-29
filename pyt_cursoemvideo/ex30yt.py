velo = int(input("Qual a velocidade atual do carro? "))
multa = (velo-80)*7
if velo <= 80:
    print('Pode seguir sua viagem!')
else:
    print(f'Você estava acima do limite de velocidade,\nPagará uma multa de R${multa}!')