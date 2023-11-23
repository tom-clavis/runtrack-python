def suppr(L):
    min = L[0]
    for i in L:
        if i < min:
            min = i
    return min

def liste(L):
    print(f"La liste avant trie : {L}")
    Lc = L
    l_trier = []
    while Lc:
        l_trier.append(suppr(Lc))
        Lc.remove(suppr(Lc))
    return l_trier

L = [7, 11, 42, 39, 2]
print(liste(L))