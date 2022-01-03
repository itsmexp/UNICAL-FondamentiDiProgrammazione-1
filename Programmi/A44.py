x = input()

l1 = list(x[:len(x)//2])
l2 = list(x[len(x)//2:])

suml1, suml2 = 0, 0

for i in range(len(l1)):
    suml1 += int(l1[i])
    suml2 += int(l2[i])

if suml1 == suml2:
    print("FORTUNATO", end="")
else:
    print("SFORTUNATO", end="")