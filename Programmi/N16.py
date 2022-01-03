x = int(input())
cont = 0
contMax = 0

i = 0
while i != -1:
    i = int(input())
    if i == 0:
        cont = cont + 1
    else:
        if contMax < cont:
            contMax, cont = cont, 0
        else:
            cont = 0
if contMax >= x:
    print("OK", end = "")
else:
    print("NO", end = "")