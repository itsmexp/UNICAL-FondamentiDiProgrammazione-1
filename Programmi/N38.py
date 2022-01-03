l1 = []
l2 = []

for i in range(100):
    x = int(input())
    if x > 50 or x < -50:
        l1.append(x)
    else:
        l2.append(x)

if len(l1) != 0:
    for i in range(len(l1)):
        print(l1[i], end = "")
    print("")
else:
    print("VUOTO1")

if len(l2) != 0:
    media = sum(l2) / len(l2)
    media = round(media, 6)
    print(media, end = "")
else:
    print("VUOTO2", end = "")
