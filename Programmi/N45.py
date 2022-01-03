N = list(input())

nMin = []

while len(N) > 0:
    m = min(N)
    nMin.append(m)
    N.pop(N.index(m))

nMax = list(reversed(nMin))

Min = ""
Max = ""

for i in nMin:
    Min += i

for i in nMax:
    Max += i

print(int(Max) - int(Min), end = "")
