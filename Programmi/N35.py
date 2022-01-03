valore=1
somma=0
while valore!=0:
    valore=int(input())
    if valore!=0:
        misura=input()
        if misura=="s":
            somma+=valore
        elif misura=="m":
            somma+=valore*60
        elif misura=="h":
            somma+=valore*3600
print(somma,end="")
