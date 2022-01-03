l1 = []
l2 = []

x = ""
while x != ".":
    x = input()
    l1.append(x)
x = ""
while x != ".":
    x = input()
    l2.append(x)

disgiunte = True
carattere = ""

for i in range(len(l1)-1):
    if disgiunte:
        for j in range(len(l2)-1):
            if l1[i] == l2[j]:
                disgiunte = False
                carattere = l1[i]
    else:
        break

if disgiunte:
    print("DISGIUNTE", end="")
else:
    print(carattere, end = "")