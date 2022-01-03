materiale = int(input()) 
ore = int(input())

costo = materiale + 40 * ore
if costo > 100:
    print(costo, end = "")
else:
    print(100, end = "")