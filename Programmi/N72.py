nStudenti = 90

rEsatte = list(input())
matricola = []
risposte = []
voto = []

for i in range(nStudenti):
    matricola.append(input())
    risposte.append(list(input()))

for i in range(nStudenti):
    votazione = 0
    for j in range(20):
        if risposte[i][j] != "X":
            if risposte[i][j] == rEsatte[j]:
                votazione += 2
            else:
                votazione -= 1
    voto.append(votazione)

for i in range(nStudenti):
    print(matricola[i], voto[i])