Stringa=str(input())
Non_Sono_tutte_Lettere=bool(True)
Risposta=""
Lunghezza=len(Stringa)
N=Stringa

if Lunghezza==1:
    while N!=".":
        L=len(N)
        if L==1:
            if N.isalpha()==True:
                Non_Sono_tutte_Lettere=False
        N=str(input())




if Non_Sono_tutte_Lettere==True or Stringa==".":
    Risposta="SI"
else:
    Risposta="NO"

if Stringa!="":
    print(Risposta,end="")
