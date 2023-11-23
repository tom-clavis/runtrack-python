def calcul(L):
    nb = 1
    for i in L:
        if 90>=i>=25:
            nb *= i
    print(nb)

L=[8,24,27,48,2,16,9,7,84,91]
calcul(L)