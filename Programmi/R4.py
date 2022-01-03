def ricSost(l, x, somma):
    occ = 0
    while x in l:
        l[l.index(x)] = 0
        occ = occ + 1
    if occ == 0:
        return somma
    else:
        return ricSost(l, occ, somma+occ)


def main():
    x = int(input())
    n = int(input())
    l = []
    for i in range(n):
        l.append(int(input()))
    print(ricSost(l, x, 0), end = "")

main()