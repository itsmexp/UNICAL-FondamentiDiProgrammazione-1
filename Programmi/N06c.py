from math import *

chiamate = int(input())
costo = 5

chiamate = chiamate - 80

i = 0
while chiamate > 0:
    chiamate = chiamate - 1
    if i < 60:
        costo = costo + 0.10
    elif i < 110:
        costo = costo + 0.07
    else:
        costo = costo + 0.05
    
    i = i + 1

print(round(costo, 3), end = "")