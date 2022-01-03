Stringa=str(input())
Cè_una_Lettera=bool(False)
Risposta=""
Lunghezza=len(Stringa)
N=Stringa

if Lunghezza==1:
    while N!=".":
        L=len(N)
        if L==1:
            if N.isalpha()==True:
                Cè_una_Lettera=True
        N=str(input())




if Cè_una_Lettera==True:
    Risposta="SI"
elif Stringa==".":
    Risposta="NO"
else:
    Risposta="NO"

if Stringa!="":
    print(Risposta,end="")
