def main():
    mat = []

    num = -1
    while num != 0:
        num = int(input())
        mat.append(num)
    
    mat.pop()
    andamento = 0
    #0 cresc 1 dec -1 err

    if len(mat) <= 2 or mat[0] >= mat[1]:
        andamento = -1
    else:
        for i in range (1, len(mat)-1):
            if mat[i] > mat[i+1] and andamento == 0:
                andamento = 1
            elif mat[i] < mat[i+1] and andamento == 1:
                andamento = -1
                break
            if mat[i] == mat[i+1]:
                andamento = -1
                break
        
    if andamento != 1:
        print("NO", end = "")
    else:
        print("SI", end = "")


main()