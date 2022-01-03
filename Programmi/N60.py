S = input()
N = int(input())
l = []
for i in range(N):
    l.append(input())

conc = False
for i in range(N):
    for j in range(N):
        if i != j and S == l[i]+l[j]:
            conc = True
            break
    if conc:
        break

if conc:
    print("OK", end = "")
else:
    print(max(l)+min(l), end = "")