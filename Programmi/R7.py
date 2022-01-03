def mcd(a, b):
    resto = a % b
    if resto == 0:
        return b
    return mcd(b, resto)

def main():
    a = int(input())
    b = int(input())

    print(mcd(a, b), end = "")

main()
