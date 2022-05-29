n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
n3 = int(input("Terceiro valor: "))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
elif n3<n1 and n3<n2:
    menor = n3
print(f"O menor valor digitado é {menor}")
maior = n2
if n1>n2 and n1>n3:
    maior = n1
elif n3>n1 and n3>n2:
    maior = n3
print(f"O maior valor digitado é {maior}")
