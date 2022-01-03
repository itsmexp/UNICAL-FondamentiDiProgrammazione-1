N = int(input())
Candidato1 = 0
Candidato2 = 0
Candidato3 = 0
if N != 0:
    while N != 0:
        if N == 1:
            Candidato1 += 1
        elif N == 2:
            Candidato2 += 1
        else:
            Candidato3 += 1
        N = int(input())
    VotiTotali = Candidato1+Candidato2+Candidato3
    Percentuale1 = round(Candidato1/VotiTotali*100, 1)
    Percentuale2 = round(Candidato2/VotiTotali*100, 1)
    Percentuale3 = round(Candidato3/VotiTotali*100, 1)
    print(1, Candidato1, Percentuale1)
    print(2, Candidato2, Percentuale2)
    print(3, Candidato3, Percentuale3)
    if (Percentuale1 > 50 or Percentuale2 > 50 or Percentuale3 > 50):
        if Percentuale1 > Percentuale2:
            if Percentuale1 > Percentuale3:
                print("VINCE 1", end="")
            else:
                print("VINCE 3", end="")
        elif Percentuale2 > Percentuale3:
            print("VINCE 2", end="")
        else:
            print("VINCE 3", end="")
    else:
        print("BALLOTTAGGIO", end="")
else:
    print("BALLOTTAGGIO", end="")


