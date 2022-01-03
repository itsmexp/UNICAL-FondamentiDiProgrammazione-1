stringa=str(input())
presente=False
N=stringa
if len(stringa)==1:
    while N!="*":
        L=len(N)
        if L==1:
            if N.isdigit():
                presente=True

        N=str(input())

if presente==False or stringa=="*":
    print("NESSUNA",end="")
else:
    print("ALMENO UNA",end="")


