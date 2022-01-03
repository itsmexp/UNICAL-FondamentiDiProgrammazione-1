consecutivi_uguali= False
last = "asd"
lettera=str
Risposta=str("")
while lettera!= "*":
    lettera = input()

    if(lettera == "*"):
        break

    if(lettera == last):
        consecutivi_uguali = True

    last = lettera

if consecutivi_uguali:
    Risposta="SI"
else:
    Risposta="NO"

if Risposta!="":
    print(Risposta,end="")
