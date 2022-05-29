# MÉDIA
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))
media = (nota1 + nota2 + nota3)/3
print(f"Sua média é {media}")
if (7 > media >= 5):
    print("Com a média {:.2f}, você está de RECUPERACAÇÃO".format(media))
elif (media < 5):
    print("Você está REPROVADO. Sua média foi {:.2f}".format(media))
else:
    print("Sua média foi {:.2f}, você PASSOU!".format(media))
