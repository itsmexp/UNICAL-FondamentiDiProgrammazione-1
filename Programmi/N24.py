vocale_last = False
vocali = "aeiou"
sequenze = 1

lettera = input()
vocale_last = bool(lettera in vocali)
if(lettera == "."):
    sequenze = 0
else:
    while lettera != ".":
        lettera = input()

        if(lettera == "."):
            break

        if((lettera in vocali)==vocale_last):
            sequenze += 1
        

        vocale_last = bool(lettera in vocali)

    
print(sequenze, end="")
