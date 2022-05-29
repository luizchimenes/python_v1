# GERENCIADOR DE PAGAMENTOS
price = float(input("Preço total das compras: R$"))
print('''FORMAS DE PAGAMENTO
[1] à vista no dinheiro/cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
while True:
    option = int(input("Qual opção você gostaria: "))
    if (option == 1):
        print("O preço de {} vai para {:.2f} com 10% de desconto".format(price,(price*(90/100))))
        break
    elif ( option == 2):
        print("O preço de {} vai para {:.2f} com 5% de desconto".format(price,(price*(95/100))))
        break
    elif (option == 3):
        print("O preço será {}".format(price))
        break
    elif (option == 4):
        parc = int(input("Em quantas parcelas deseja fazer? "))
        total = (price*120/100)/parc
        print("O valor de {} vai para {:.2f} com 20% de juros em {}x parcelas de R${}".format(price,(price*(120/100)),parc,total))
        break
    else: 
        print("VALOR INVÁLIDO. TENTE NOVAMENTE")