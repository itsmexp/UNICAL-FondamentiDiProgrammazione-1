a = int(input())
b = int(input())
c = int(input())

if not(a + b > c and a + c > b and b + c > a):
    print("NO", end = "")
elif a == b and b == c:
    print("TRIANGOLO EQUILATERO", end = "")
elif a == b or b == c:
    print("TRIANGOLO ISOSCELE", end = "")
else:
    print("TRIANGOLO SCALENO", end = "")
