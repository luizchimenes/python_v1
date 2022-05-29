sal = float(input("Qual seu salário atual?:R$"))
au = sal*(115/100)
print("Parábens, você recebeu um aumento de 15%. O seu salário de R${:.2f} aumentou para R${:.2f}!".format(sal,au))