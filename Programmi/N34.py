x = int(input())
l = []
for i in range(x):
    l.append(int(input()))

cond = True
if x == 0:
    cond = True
else:
    for i in range(1, len(l), 2):
        if l[i] % 2 == 0:
            cond = False
            break

    if cond:
        for i in range(2, len(l), 2):
            if l[i] <= l[i - 2]:
                cond = False
                break

if cond:
    print("SI", end = "")
else:
    print("NO", end = "")