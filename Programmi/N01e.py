conto = int(input())
canone = int(input())
percInt = int(input())
print("PRIMO MESE:", conto)
conto = conto - canone
interessi = (conto / 100) * percInt
conto = conto + interessi
conto = round(conto)
print("SECONDO MESE:", conto)
conto = conto - canone
interessi = (conto / 100) * percInt
conto = conto + interessi
conto = round(conto)
print("TERZO MESE:", conto, end="")