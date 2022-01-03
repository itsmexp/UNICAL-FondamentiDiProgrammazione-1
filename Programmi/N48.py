def riempiMat():
    x = 0
    mat = []
    while x >= 0:
        x = int(input())
        mat.append(x)
    return mat 


def seqMassima(mat):
    l = []
    lmax = []
    x = 0
    for i in range(len(mat)-1):
        l.append(mat[i])
        if mat[i] > mat[i+1]:
            if len(l) > len(lmax):
                lmax.clear()
                lmax = list(l)
            l.clear()
    if len(l) > len(lmax):
        lmax.clear()
        lmax = list(l)
    return lmax        


def stampaSec(l):
    if len(l) == 0:
        print("Empty", end = "") 
    else:
        for i in l:
            print(i, end="")
        print()
        print(len(l), end ="")


def main():
    mat = riempiMat()
    l = seqMassima(mat)
    stampaSec(l)


main()