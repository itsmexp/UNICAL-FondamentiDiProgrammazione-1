x = int(input(""))
n = int(input(""))

seq = ""
while n > 0:
    a = int(input(""))
    if a < x and a % 2 == 0:
        seq += str(a)
    n -= 1
print(seq, end = "")