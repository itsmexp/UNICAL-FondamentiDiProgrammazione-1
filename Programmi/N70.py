frase = list(input())
fraseConvertita = []

vocali = ["a","e","i","o","u"]

for i in frase:
    fraseConvertita.append(i)
    if i in vocali:
        fraseConvertita.append("f")
        fraseConvertita.append(i)

for i in fraseConvertita[len(fraseConvertita)//2:]:
    print(i, end = "")
for i in fraseConvertita[:len(fraseConvertita)//2]:
    print(i, end = "")