# IMC
peso = float(input("Digite seu peso(kg): "))
altura = float(input("Digite sua altura(m): "))
imc = peso / (altura**2)
print("Seu IMC é {:.1f}!".format(imc))
if (imc < 18.5):
    print("Você está ABAIXO DO PESO")
elif ( imc < 25):
    print("Você está no PESO IDEAL. PARABÉNS")
elif ( imc < 30):
    print("Você está em SOBREPESO")
elif ( imc < 40):
    print("Você está OBESO")
else: 
    print("Você é um OBESO MÓRBIDO")