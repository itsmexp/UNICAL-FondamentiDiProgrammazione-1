mese=int(input())

if mese<=0 or mese>12:
    print("MESE NON VALIDO",end="")
    
elif mese==12:
    giorno=int(input())
    if giorno>=1 and giorno<=20:
        print("AUTUNNO", end="")
    else:
        print("INVERNO", end="")
    
elif mese==1 or mese==2:
    print("INVERNO",end="")

elif mese==3:
    giorno=int(input())
    if giorno>=1 and giorno<=20:
        print("INVERNO", end="")
    else:
        print("PRIMAVERA", end="")

elif mese==4 or mese==5:
    print("PRIMAVERA",end="")

elif mese==6:
    giorno=int(input())
    if giorno>=1 and giorno<=20:
        print("PRIMAVERA", end="")
    else:
        print("ESTATE", end="")

elif mese==7 or mese==8:
    print("ESTATE",end="")

elif mese==9:
     giorno=int(input())
     if giorno>=1 and giorno<=20:
         print("ESTATE", end="")
     else:
         print("AUTUNNO",end="")

elif mese==10 or mese==11:
    print("AUTUNNO",end="")
