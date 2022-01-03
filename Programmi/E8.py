N = int(input())

mat = [[int(input()) for i in range(N)] for j in range(N)]

l = []
ripetizioni = False

for i in range(N):
    for j in range(N):
        if mat[i][j] not in l:
            l.append(mat[i][j])
        else:
            ripetizioni = True
    if ripetizioni:
        break
    l.clear()

if not ripetizioni:
    for j in range(N):
        for i in range(N):
            if mat[i][j] not in l:
                l.append(mat[i][j])
            else:
                ripetizioni = True
        if ripetizioni:
            break
        l.clear()

if not ripetizioni:
    print("SI", end = "")
else:
    print("NO", end = "")