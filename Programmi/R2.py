def main():
    N = int(input())
    l = []
    for i in range(N):
        l.append(int(input()))
    if N%2 != 0:
        print("NO", end = "")
    elif verUguaglianza(N, 0, l):
        print("SI", end = "")
    else:
        print("NO", end = "")


def verUguaglianza(N, i, A):   
    if i == (N//2):
        return True
    if A[i] == A[(N//2)+i]:
        i=i+1
        return verUguaglianza(N, i, A)
    else:
        return False


main()