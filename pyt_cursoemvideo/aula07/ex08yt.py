met = float(input("Digite uma medida em metros:"))
c = met*100
m = met*1000
d = met*10
da = met/10
h = met/100
k = met/1000
print("{}m em quilômetros é {}km\nEm hectômetros é {}ha\nEm decâmetros é {}da\nEm decímetros é {}dm\nEm centímetros é {}cm\nE em milímetros é {}mm".format(met,k,h,da,d,c,m))