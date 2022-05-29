#   Tabuada v3.0 - interrompido quando o valor digitado for negativo
mult = 1
print('\033[34mTABUADA 3.0\033[m')
print(10*'-=')
while True:
    num = int(input('Digite um número ( negativo para parar ): '))
    print(10*'-=')
    if num < 0:
        print("PROGRAMA DE TABUADA ENCERRADO")
        break
    while mult <= 10:
        prod = num * mult
        print(f'{num} x {mult} = {prod}')
        mult += 1
    print(10*'-=')