frase = input()
alfabeto = list("abcdefghijklmnlopqrstuvwyz")

pangramma = True
for i in alfabeto:
    if i not in frase:
        pangramma = False

if pangramma:
    print("SI", end= "")
else:
    print("NO", end = "")