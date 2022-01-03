Stringa=str(input())
Tappo=str("*")
Presente=bool(False)
Risposta=""
Str1=Stringa

if Stringa!=Tappo:
    while Str1!=Tappo :
        if Str1=="a"or Str1=="e" or Str1=="i" or Str1=="o" or Str1=="u":
            Presente=True
        Str1=str(input())
else:
    Risposta="NESSUNA VOCALE"

if Presente==False:
    Risposta="NESSUNA VOCALE"
else:
    Risposta="ALMENO 1 VOCALE"


if Risposta!="":
    print(Risposta,end="")
    
        
            
