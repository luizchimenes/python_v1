nome = str(input("Digite seu nome completo: ")).strip()
print("Analisando seu nome")
print("Seu nome maiúsculo é {}".format(nome.upper()))
print("Seu nome tem {} letras".format(len(nome) - nome.count(" ")))
separa = nome.split()
print("Seu primeiro nome é {} e ele tem {} letras".format(separa[0], len(separa[0])))
#print("Seu primeiro nome tem {} letras".format(nome.find(' ')))