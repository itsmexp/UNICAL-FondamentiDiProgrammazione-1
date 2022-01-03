conto = 500
print("PRIMO MESE:", conto)
conto = conto - 5
interessi = (conto / 100) * 2
conto = conto + interessi
conto = round(conto)
print("SECONDO MESE:", conto)
conto = conto - 5
interessi = (conto / 100) * 2
conto = conto + interessi
conto = round(conto)
print("TERZO MESE:", conto, end="")