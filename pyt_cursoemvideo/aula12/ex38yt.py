# Conversor de bases - Binário, Octal e Hexadecimal
num = int(input("Digite um número inteiro: "))
print('''Escolha uma das bases para conversão
[1] converter para binário
[2] coverter para octal
[3] converter para hexadecimal''')
print(20*'=-=')
option = int(input("Sua opção é: "))
print(20*"-=-")
if (option == 1):
    print(f"Seu número convertido para binário é {bin(num)[2:]}")
elif (option == 2):
    print(f"Seu número convertido em OCTAL é {oct(num)[2:]}")
elif (option == 3):
    print(f"Seu número convertido em HEXADECIMAL é {hex(num)[2:]}")
else:
    print("OPÇÃO INVÁLIDA")