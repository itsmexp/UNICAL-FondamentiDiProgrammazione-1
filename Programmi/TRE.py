x = int(input())
mat = []
for i in range(10):
    mat.append([0]*10)
val = 1
for i in range(10):
    for j in range(10):
        mat[i][j] = val
        if val < x:
            val+=1
        else:
            val = 1

somma = 0
for i in range(10):
    somma += mat[i][9-i]

print(somma, end="")