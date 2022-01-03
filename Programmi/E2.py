N = int(input())
mat = [[int(input()) for i in range(N)] for j in range(N)]

lCol = [int(input()) for i in range(N)]
lRighe =  [int(input()) for i in range(N)]

errore = False

for i in range(N):
    if mat[i].count(1) != lRighe[i]:
        errore = True
        break

if not errore:
    for j in range(N):
        cont = 0
        for i in range(N):
            if mat[i][j] == 1:
                cont += 1
        if cont != lCol[j]:
            errore = True
            break

if not errore:
    print("SI", end = "")
else:
    print("NO", end = "")
