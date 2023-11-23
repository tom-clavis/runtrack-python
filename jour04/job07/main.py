def calcul(L):
    nb = 0
    for i in L :
        if i%3 == 0 :
            nb += 1
    print(nb)

L=[8,24,48,2,16]
calcul(L)