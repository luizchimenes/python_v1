salario = float(input("Qual o salário do funcionário? R$"))
if salario > 1250:
    novo_1 = salario*(110/100)
    print(f'Seu novo salário é R${novo_1}!')
else:
    novo_2 = salario*(115/100)
    print(f"Seu novo salário é R${novo_2}!")