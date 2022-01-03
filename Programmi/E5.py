x = 0 
l = []

alfabeto = list("abcdefghijklmnopqrstuvwxyz*")

while x != "*":
    x = input()
    l.append(x)


primoCarattereDef = -1
primoCarattere = -1
lSeqMax = 1
lSeq = 1

for i in range(len(l)-1):
    if alfabeto.index(l[i]) >= alfabeto.index(l[i+1]):
        if lSeq == 1:
            primoCarattere = i
        lSeq += 1
    else:
        if lSeq >= 2 and lSeqMax <= lSeq:
            primoCarattereDef = primoCarattere
            lSeqMax = lSeq
        lSeq = 1

if lSeqMax < lSeq:
    primoCarattereDef = primoCarattere
    lSeqMax = lSeqMax    

if not(primoCarattereDef == -1 or lSeqMax == 1):
    print(alfabeto.index(l[primoCarattereDef]) - alfabeto.index(l[primoCarattereDef + lSeqMax - 1]) - 1, end = "")
else:
    print(0, end = "")