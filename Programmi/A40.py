l = []
i = 0
while i != -50:
    i = int(input())
    l.append(i)

l.pop()
if len(l) == 0:
    print("VUOTA", end = "")
else:
    media = sum(l) // len(l)
    x = True
    while x:
        if min(l) < media:
            l.pop(l.index(min(l)))
        else:
            x = False
    print(min(l), end = "") 
