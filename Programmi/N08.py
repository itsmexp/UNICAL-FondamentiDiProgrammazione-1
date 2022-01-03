a = int(input())
b = int(input())
somma = 0

if a % 2 == 0:
    for i in range(a+1, b+1, 2):
        somma += i
else:
    for i in range(a, b+1, 2):
        somma += i

print(somma, end = "")