n = 0
a = -1
while a != 0:
    a = int(input())
    if a%3 == 0 and a%2 == 1:
        n += 1
print(n, end = "")