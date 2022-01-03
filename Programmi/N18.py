stringa=str()
S=stringa
cont=0
while cont!=1:
    N=S
    S=str(input())
    X=len(S)
    if X==1:
        if S=="k" and N=="o":
            cont=1
        else:
            stringa+=S
            cont=0
    else:
        cont=0

if stringa!="":
    X=len(stringa)
    print(X-1,end="")
