def inverti(l, linv):
    if len(linv) == len(l):
        return linv
    linv.append(l[len(l) - len(linv) - 1])
    return inverti(l, linv)


def main():
    n = int(input())
    list = []
    listInv = []
    for i in range(n):
        list.append(int(input()))

    listInv = inverti(list, listInv)
    for i in listInv:
        print(i, end = "")


main()