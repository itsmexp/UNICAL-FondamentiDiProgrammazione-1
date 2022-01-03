from math import *

costo = float(input())
condizione = int(input())

if condizione == 1:
    costo = costo - ((costo / 100) * 10)
elif condizione == 2:
    costo = costo - ((costo / 100) * 15)
elif condizione == 3:
    costo = costo - ((costo / 100) * 25)

print(round(costo, 3), end = "")