dist = float(input("Qual foi a distância percorrida na sua viagem? "))
# preco = dist*0.50 if dist <=200 else dist * 0.45
if dist <= 200:
    print("A sua viagem de {}Km custará R${:.2f}.".format(dist, (0.50*dist)))
else:
    print("A sua viagem de {}Km custará R${:.2f}.".format(dist, (dist*0.45)))