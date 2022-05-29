n = 0
while True:
    idade = int(input("Digite sua idade: "))
    if (idade < 0):
        break
    altura = float(input("Agora digite sua altura: "))
    if (idade >= 18) and (altura > 1.60):
        n += 1
print("{} pessoas de 18 anos possuem mais de 1.60 metros".format(n))
