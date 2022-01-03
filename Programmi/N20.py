stringa=str(input())
tutte_lettere=False
N=stringa
if len(stringa)==1:
    while N!=".":
        if len(N)==1:
            if N.isalpha()==False:
                tutte_lettere=True
        N=str(input())

if tutte_lettere==False or stringa==".":
    print("SI",end="")
else:
    print("NO",end="")
