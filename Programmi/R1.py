def f(N):
    if N == 0:
        return 2
    else:
        return 3 * (N+1) * f(N-1)


def main():
    i = int(input())
    print(f(i), end = "")


main()