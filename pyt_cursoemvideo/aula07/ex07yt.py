n1 = float(input("Digite sua primeira nota:"))
n2 = float(input("Digite dua segunda nota:"))
n3 = float(input("Digite sua última nota:"))
nm = (n1+n2+n3)/3
print("Sua média é {:.1f}!".format(nm))
if (nm >= 9):   # inventei essa parte
    print("Tu é pika")
elif (nm >= 6):
    print("Aprovado")
else:
    print("Se Fodeu")

