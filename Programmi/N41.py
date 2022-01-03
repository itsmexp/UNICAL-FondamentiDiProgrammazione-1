def scegliPosto(mat):
    ris = input("Digitare 1 per fumatori o 2 per non fumatori:")
    if ris == "1":
        if 0 in mat[:5]:
            pos = mat.index(0)
            mat[pos] = 1
            print("Reparto fumatori, posto", pos+1)
        else:
            scelta = input("Reparto scelto al completo. Si desidera un posto nell'altro reparto (S/N)?")
            if scelta == "S":
                pos = mat[5:].index(0)
                mat[pos+5] = 1
                print("Reparto NON fumatori, posto", pos+6)
            else:
                print("Il prossimo volo parte tra 3 ore")
    else:
        if 0 in mat[5:]:
            pos = mat[5:].index(0)
            mat[pos+5] = 1
            print("Reparto NON fumatori, posto", pos+6)
        else:
            scelta = input("Reparto scelto al completo. Si desidera un posto nell'altro reparto (S/N)?")
            if scelta == "S":
                pos = mat[:5].index(0)
                mat[pos] = 1
                print("Reparto fumatori, posto", pos+1)
            else:
                print("Il prossimo volo parte tra 3 ore")


def main():
    mat = [0]*10
    while 0 in mat:
        scegliPosto(mat)
    

main()