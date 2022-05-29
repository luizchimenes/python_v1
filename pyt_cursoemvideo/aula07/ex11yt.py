larg = float(input("Largura da parede:"))
alt = float(input("Altura da parede:"))
area = larg*alt
print("Sua parede possui a dimensao de {} por {} e sua área é {:.2f}".format(larg,alt, (larg*alt)))
print("Você precisará de {:.2f} litros de tintas".format(area/2))