def sommaLin(N, mat):
    somma = 0
    for i in range(N):
        somma += mat[i][N-i-1]
    return somma

def sommaRic(mat,N,i):
     somma = 0
     if N==0:
          return mat[N][i]
     elif N!=0:
          somma += mat[N][i]
     return somma + sommaRic(mat,N-1,i+1)

def main():
    N = int(input())
    mat = []
    for i in range(N):
        mat.append([0]*N)

    for i in range(N):
        for j in range(N):
            mat[i][j] = int(input())

    print(sommaLin(N, mat), sommaRic(mat, N-1, 0), sep = ";", end="")

main()