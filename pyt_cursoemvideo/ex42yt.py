# CLASSIFIACAR ATLETAS
idade = int(input("Digite a IDADE do atleta: "))
if (idade > 25):
    print("O atleta é da categoria \033[34mMASTER\033[m.")
elif ( 19 < idade <= 25):
    print("O atleta é da categoria \033[34mSÊNIOR\033[m.")
elif (14 < idade <= 19):
    print("O atleta é da categoria \033[34mJÚNIOR\033[m.")
elif (9 < idade <= 14):
    print("O atleta é da categoria \033[34mINFANTIL\033[m.")
else:
    print("O atleta é da categoria \033[34mMIRIM\033[m.")
