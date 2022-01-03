semeb=int(input())
seme1=int(input())
carta1=float(input())
seme2=int(input())
carta2=float(input())

if carta1==1:
    carta1=11
elif carta1==3:
    carta1=10.5

if carta2==1:
    carta2=11
elif carta2==3:
    carta2=10.5

##no briscole
if (seme1!=semeb and seme2!=semeb):
    if ((seme1==seme2)and (carta1>carta2)):
        print("VINCE GIOCATORE 1", end="")
    elif ((seme1==seme2)and(carta1<carta2)):
        print ("VINCE GIOCATORE 2", end="")
    elif(seme1!=seme2):
        print("VINCE GIOCATORE 1", end="")

##casi briscole
if (seme1==semeb and seme2!=semeb):
    print("VINCE GIOCATORE 1", end="")

elif(seme1!=semeb and seme2==semeb):
    print("VINCE GIOCATORE 2", end="")

elif(seme1==semeb and seme2==semeb):
    if (carta1>carta2):
        print("VINCE GIOCATORE 1", end="")
    else:
        print("VINCE GIOCATORE 2", end="")

