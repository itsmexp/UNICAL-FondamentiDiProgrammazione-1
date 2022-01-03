M = input()

validità = True

for i in range(len(M)):
    if i == 0 and not(M[i].isalpha() or M[i] == "_"):
        validità = False
        break
        
    elif not(M[i].isalnum() or M[i] == "_"):
        validità = False
        break

if validità:
    print("SI", end = "")
else:
    print("NO", end = "")