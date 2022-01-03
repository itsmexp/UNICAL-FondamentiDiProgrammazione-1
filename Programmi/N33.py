from random import randint
from random import seed


primo_giocatore = int
pc = int

vincePC = 0
vinceG = 0
pari = 0

vittoriaG = 0
vittoriaPC = 0

sasso = 1
carta = 2
forbice = 3


while vittoriaG != 3 and vittoriaPC != 3:
    primo_giocatore = int(input("Inserisci la giocata del primo giocatore (1: sasso, 2: carta, 3: forbice):"))

    if primo_giocatore == 1 or primo_giocatore == 2 or primo_giocatore == 3:
        seed(0)
        pc = randint(1,3)
        
    if primo_giocatore == 1:
        print("hai giocato sasso")
    elif primo_giocatore == 2:
        print("hai giocato carta")
    elif primo_giocatore == 3:
        print("hai giocato forbice")
        

    if pc == 1:
        print("il PC ha giocato sasso")
    elif pc == 2:
        print("il PC ha giocato carta")
    elif pc == 3:
        print("il PC ha giocato forbice")


    if primo_giocatore == pc:
        print("Pari:")
        print(vittoriaG,"-",vittoriaPC,sep="")
    elif (primo_giocatore == 1 and pc == 3) or (primo_giocatore == 2 and pc == 1) or (primo_giocatore ==3 and pc == 2):
        vittoriaG += 1
        vittoriaPC = 0
        print("Vinci tu:")
        print(vittoriaG,"-",vittoriaPC,sep="")
    elif (primo_giocatore == 1 and pc == 2) or (primo_giocatore == 2 and pc == 3) or (primo_giocatore == 3 and pc == 1):
        vittoriaG = 0
        vittoriaPC += 1
        print("Vince il PC:")
        print(vittoriaG,"-",vittoriaPC,sep="")
        
        
    vittoriaG = vittoriaG
    vittoriaPC = vittoriaPC


if vittoriaG == 3:
    print("Hai vinto la sfida!",end="")
elif vittoriaPC == 3:
    print("Il PC ha vinto la sfida!",end="")
