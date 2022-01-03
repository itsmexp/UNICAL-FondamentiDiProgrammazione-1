from math import log2

x = -1
l = []
while x != 0:
    x = int(input())
    l.append(x)

l.pop()
potenza = True

for i in range(len(l)):
    if log2(l[i])%1 != 0:
        potenza = False
    
if potenza:
    print("SI", end = "")
else:
    print("NO", end = "")