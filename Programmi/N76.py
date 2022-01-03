M = int(input())
N = int(input())

mat = []

giudiceVotoMax = []
concorrenteSommaVoti = []

for i in range(M):
    mat.append([])
    for j in range (N):
        mat[i].append(int(input()))

for i in range(M):
    giudiceVotoMax.append(0)
    for j in range (N):
        if mat[i][j] > 5:
            giudiceVotoMax[i] += 1 

for i in range(N):
    concorrenteSommaVoti.append(0)
    for j in range(M):
        concorrenteSommaVoti[i] += mat[j][i]

votoMax = max(giudiceVotoMax)
SommaVotiMin = min(concorrenteSommaVoti)

giudiceVotoMax.reverse()
concorrenteSommaVoti.reverse()

print(M - giudiceVotoMax.index(votoMax) - 1, end = " ")
print(N - concorrenteSommaVoti.index(SommaVotiMin) - 1, end = "")
