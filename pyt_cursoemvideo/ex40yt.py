# Alistamento Militar
from datetime import date
sexo = str(input("Você é Homem ou Mulher: [H/M]: "))
if sexo == "H":
    atual = date.today().year
    ano = int(input("Digite seu ano de nascimento: "))
    alist = atual  - ano
    if (alist == 18):
        print("Você deve se alistar nesse ano!")
    elif(alist < 18):
        print(f"Ainda não chegou a hora! Faltam {18 - alist} anos para o seu alistamento.")
        print(f"Seu alistamento será em {atual + (18 - alist)}!")
    else:
        print(f"Já passou da hora de se alistar. Seu alistamento foi há {alist - 18} anos.")
        print(f"Seu alistamento foi em {atual - (alist - 18)}!")
else:
    print("Você NÃO PRECISA se alistar!")
