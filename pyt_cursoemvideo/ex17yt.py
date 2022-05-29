import math
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hip = math.hypot(co,ca)
# hip = (co ** 2 + ca ** 2) ** (1/2)
print("A hipotenusa vale {:.2f}.".format(hip))
