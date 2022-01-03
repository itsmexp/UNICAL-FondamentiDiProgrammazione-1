l = []
vocale = ["a", "e", "i", "o", "u"]
for i in range(100):
    l.append(input())   

voc = 5
# 0:a 1:e 2:i 3:o 4:u
# 6: errore
for i in range(100):
    if l[i] in vocale:
        if voc == 5:
            voc = vocale.index(l[i])
        else:
            if voc != vocale.index(l[i]):
                voc = 6
                break

if voc == 6:
    print("ERRORE", end = "")
else:
    print("OK", end = "") 
