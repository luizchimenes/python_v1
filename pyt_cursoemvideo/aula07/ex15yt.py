dia = int(input("Por quantos dias o carro foi alugado?:"))
km = float(input("Quantos km foram rodados com o carro?:"))
total = (60*dia) + (0.15*km)
print("O total a pagar é R${:.2f}.".format(total))
