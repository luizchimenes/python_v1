# Maior e menor valores na Lista - Ler 5 números
lista = [int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: ')),
int(input('Digite o terceiro número: ')), int(input('Digite o quarto número: ')), 
int(input('Digite o quinto número: '))]
print(15*'-=-')
print(f'A lista final é {lista}')
print(15*'-=-')
print(f'O \033[34mMAIOR\033[m número é \033[34m{max(lista)}\033[m que se encontra na posição {lista.index(max(lista)) + 1}')
print(f'O \033[31mMENOR\033[m número é \033[31m{min(lista)}\033[m que se encontra na posição {lista.index(min(lista)) + 1}')
print(f'{"FIM DO PROGRAMA":^40}')