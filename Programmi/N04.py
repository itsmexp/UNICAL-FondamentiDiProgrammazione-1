a = int(input())

if a < 0 or a > 30:
    print("VOTO NON VALIDO", end = "")
elif a >= 18:
    print("ESAME SUPERATO", end = "")
else:
    print("BOCCIATO", end = "")