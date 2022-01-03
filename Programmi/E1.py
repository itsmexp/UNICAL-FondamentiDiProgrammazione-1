def validaNome(stringa):
    for i in range(len(stringa)):
        if i == 0 and not(stringa[i].isalpha() or stringa[i] == "_"):
            return False   
        elif not(stringa[i].isalnum() or stringa[i] == "_"):
            return False
    return True


def validaFunzione(fun):
    if len(fun) < 5:
        return False
    if fun[0] != "def" or fun[2] != "(" or fun[len(fun)-2] != ")":
        return False
    if validaNome(fun[1]):
        if len(fun) == 5:
            return True
        elif len(fun) == 6:
            return validaNome(fun[3])
        else:
            if fun[len(fun)-3] == ",":
                return False
            if not validaNome(fun[3]):
                return False
            for i in range(4, len(fun)-3, 2):
                if fun[i] == ",":
                    if not validaNome(fun[i+1]):
                        return False
                else:
                    return False
    else:
        return False


def main():
    x = ""
    fun = []
    while x != ":":
        x = input()
        fun.append(x)

    if validaFunzione(fun):
        print("SI", end = "")
    else:
        print("NO", end = "")


main()