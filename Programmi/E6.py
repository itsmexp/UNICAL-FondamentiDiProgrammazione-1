N = int(input())
X = int(input())

l = [] 

lAnni = []
lPresenze = []
lRiproduzioni = []

for i in range(N):
    l.append([])
    riproduzioni = int(input())
    l[i].append(riproduzioni)
    anno = int(input())
    l[i].append(anno)
    if anno not in lAnni:
        lAnni.append(anno)
        lPresenze.append(1)
        lRiproduzioni.append(riproduzioni)
    else:
        lPresenze[lAnni.index(anno)] += 1
        lRiproduzioni[lAnni.index(anno)] += riproduzioni
    
maxPresenze = lPresenze.index(max(lPresenze))
print(lAnni[maxPresenze], end = " ")

if X not in lAnni:
    print("NO", end = "")
else:
    if lRiproduzioni[lAnni.index(X)] == 0:
        print("SI", end = "")
    else:
        print("NO", end = "")