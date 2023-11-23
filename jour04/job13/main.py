def clean(L):
    print(L)
    Lc = L
    L_clean = []
    while Lc:
        valeur = Lc[0]
        print(valeur)
        L_clean.append(valeur)
        for val in Lc:
            if valeur == val:
                Lc.remove(val)
    print(L_clean)


L = [10,20,30,20,10,50,60,40,80,50,40]
clean(L)