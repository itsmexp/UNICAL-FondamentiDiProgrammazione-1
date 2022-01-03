l = []
while True:
    x = input()
    if x == "*":
        break
    l.append(int(x))

lSeq = 1
cont = 0

for i in range(len(l)-1):
    if l[i]+1 == l[i+1]:
        lSeq += 1
    else:
        if lSeq >= 2:
            cont += 1
        lSeq = 1

if lSeq >= 2:
    cont += 1

print(cont, end = "")
