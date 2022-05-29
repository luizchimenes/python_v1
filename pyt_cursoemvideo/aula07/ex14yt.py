temp = float(input("Qual a temperatura atual em °C?:"))
k = temp + 273
f = ((9*temp)/5) + 32
print("A temperatura {}°C vale {} graus em Kelvin e {} em Fahreinheint!".format(temp, k, f))