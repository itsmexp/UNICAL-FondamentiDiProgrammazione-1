n = int(input())

vertice = 0
for i in range(1, n):
    vertice += (2 * i - 1)

somma = 2 * vertice + (2 * n - 1)

print(somma, end = "")