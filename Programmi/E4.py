N = int(input())
M = int(input())

mat = []

for i in range(N):
    mat.append([])
    for j in range(M):
        mat[i].append(int(input()))

esCon18 = 0

for j in range(M):
    for i in range(M):
        if mat[i][j] == 18:
            esCon18 += 1
            break

maxEsamiSostenuti = 0
mediaMax = 0

for i in range(N):
    esamiSostenuti = 0
    somma = 0
    for j in range(M):
        if mat[i][j] >= 18:
            esamiSostenuti += 1
            somma += mat[i][j]
    if esamiSostenuti > maxEsamiSostenuti:
        maxEsamiSostenuti = esamiSostenuti
        mediaMax = round(somma / esamiSostenuti)

print(M - esCon18, end = " ")
print(mediaMax, end = "")