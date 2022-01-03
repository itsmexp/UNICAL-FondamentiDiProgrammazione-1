N = list(input())
nConvertito = []
lastNumber = N[0]
cont = 1

for i in range(1,len(N)):
    if N[i] == lastNumber:
        cont += 1
    else:
        nConvertito.append(cont)
        cont = 1
        nConvertito.append(lastNumber)
        lastNumber = N[i]
nConvertito.append(cont)
nConvertito.append(lastNumber)

output = ""
for i in nConvertito:
    output += str(i)

print(output, end = "")
print(" ", end = "")
print(len(output), end = "")
