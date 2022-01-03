mat = []

char = " "
while char != "*":
    char = input()
    mat.append(char)

sodd = False
for i in range(0, len(mat)-1):
    if mat[i].isupper() and mat[i+1].isupper() and mat[i] == mat[i+1]:
        sodd = True
        break
    if mat[i].islower() and mat[i+1].islower() and mat[i] == mat[i+1]:
        sodd = True
        break

if sodd:
    print("SI", end = "")
else:
    print("NO", end = "")

