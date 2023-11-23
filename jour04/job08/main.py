def calcul(L):
    nb = 0
    for i in L :
        if i%2 == 0 :
            nb += i
    print(nb)

L=[8, 24, 27, 48, 2,16, 9, 7, 84, 91]
calcul(L)