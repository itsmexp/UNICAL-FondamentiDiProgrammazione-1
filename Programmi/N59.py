n = int(input())
mat = []

for i in range(n):
    mat.append([])
    for j in range(n):
        mat[i].append(int(input()))

sommaCroce = sum(mat[n//2])
for i in range(n):
    sommaCroce += mat[i][n//2]
sommaCroce -= mat[n//2][n//2]

somma = 0
for i in range(n):
    for j in range(n):
        somma += mat[i][j]

somma -= sommaCroce

if sommaCroce > somma:
    print("OK", end = "")
else:
    print("NO", end = "")
