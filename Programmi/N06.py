anno = int(input())

if anno % 4 == 0:
    if anno % 100 == 0 and anno % 400 != 0:
        print("NON BISESTILE", end = "")
    else:
        print("BISESTILE", end = "")
else:
    print("NON BISESTILE", end = "")