# Digitar uma expressão matemática qualquer que use parênteses / Deve analisar se a expressão
# está correta em relação aos parêntese abertos e fechados
expressao = str(input("Digite uma expressão: ")).strip()
abre = fecha = 0
for simb in expressao:
    if simb == "(":
        abre += 1
    if simb == ")":
        fecha += 1
if abre == fecha:
    print("A expressão está \033[34mCORRETA\033[m")
elif abre != fecha:
    print("A expressão é \033[31mINVÁLIDA\033[m")
print("-=- FIM DO PROGRAMA -=-")
