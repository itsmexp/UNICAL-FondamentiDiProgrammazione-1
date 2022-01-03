def lControllo(mat, x):
    if x < 2:
        return True
    somma = 0
    for i in range(x):
        somma += mat[i][len(mat[0]) - x]
    somma += sum(mat[i][len(mat[0]) - x:])
    somma -= mat[x-1][len(mat[0]) - x]
    if somma % mat[x-1][len(mat[0]) - x] == 0:
        return lControllo(mat, x-1)
    else:
        return False 

def main():
    mat = []
    n = int(input())
    for i in range(n):
        mat.append([])
        for j in range(n):
            mat[i].append(int(input()))
        
    if lControllo(mat, len(mat[0])):
        print("SI", end = "")
    else:
        print("NO", end = "")

main()
