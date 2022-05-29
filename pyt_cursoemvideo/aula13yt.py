'''n = int(input("INÍCIO: "))
f = int(input("FIM: "))
p = int(input("PASSO: "))
for c in range(n, f+1, p):
    print(c)
print("FIM")'''
soma = 0
for c in range(3):
    n = int(input("Digite um número: "))
    soma += n
print(f"A soma de todos os números é {soma}!")