A = []
B = []
for i in range(26):
    A.append(input())
N = int(input())
for i in range(N):
    B.append(int(input()))

sol = []
for i in range(len(B)):
    if B[i] >= 26:
        continue
    else:
        sol.append(A[B[i]])

if len(sol) != 0:
    for i in sol:
        print(i, end= "")