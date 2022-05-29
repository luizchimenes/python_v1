# Aprovação de Empréstimos
valor = float(input("Qual o valor da casa que deseja? R$"))
salario = float(input("Qual seu salário atual? R$"))
anos = int(input("Em quantos anos deseja pagar? "))
prest = ((valor)/(anos)/12)
if (prest > (salario*(30/100))):
    print("Empréstimo \033[34mNEGADO\033[m")
else:
    print('Sua parcela será de \033[34mR${:.2f}\033[m reais!'.format(prest))
