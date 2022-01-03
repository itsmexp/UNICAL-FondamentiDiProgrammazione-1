l = list(input())
pAperte = 0
pChiuse = 0

esito1 = True
esito2 = True

for i in l:
    if i == "(":
        pAperte += 1
    elif i == ")":
        pChiuse += 1
        if pChiuse > pAperte:
            esito1 = False
            break
if pAperte != pChiuse:
    esito1 = False

for i in range(len(l)-1):
    if l[i] == "(" and l[i+1] == ")":
        esito2 = False
        break

if esito1:
    print("ok1")
else:
    print("no1")

if esito2:
    print("ok2")
else:
    print("no2")