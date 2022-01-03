nQuesiti = 8
nStudenti = 70

peso = []
matricola = []
quesito = []

for i in range(nQuesiti):
    peso.append(int(input()))

for i in range(nStudenti):
    matricola.append(input())
    quesito.append([])
    for j in range(nQuesiti):
        quesito[i].append(int(input()))

soglia = int(input())

nAmmessi = 0
studenteMax = 0
votoMax = 0
studenteMin = 0
votoMin = 0

for i in range(nStudenti):
    voto = 0
    for j in range(nQuesiti):
        voto += (quesito[i][j] * peso[j])
    if voto >= soglia:
        print(matricola[i], voto)
        nAmmessi += 1
        if voto > votoMax:
            votoMax = voto
            studenteMax = i
        if voto < votoMin:
            votoMin = voto
            studenteMin = i

print(nAmmessi, matricola[studenteMax], matricola[studenteMin], end = "")