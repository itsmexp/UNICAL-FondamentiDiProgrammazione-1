a = input()
check = False

for i in a:
    if i == "0":
        check = True

if check:
    print("NO", end = "")
else:
    print("SI", end = "")