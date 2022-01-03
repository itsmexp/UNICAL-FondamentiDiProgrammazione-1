l = []
for i in range(10):
    l.append(int(input()))

x = int(input())
div = False
for i in range(10):
    if l[i]%x == 0:
        div = True
        break

if not div:
    print("OK", end = "")
else:
    print("NO", end = "") 