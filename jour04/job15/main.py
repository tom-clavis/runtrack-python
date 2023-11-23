def mini(L):
    min = L[0]
    for i in L:
        if i < min:
            min = i
    return min

def trie(L):
    print(f"La liste avant trie : {L}")
    Lc = L
    l_trier = []
    while Lc:
        l_trier.append(mini(Lc))
        Lc.remove(mini(Lc))
    return l_trier

def float_to_int_to_trie(L):
    Lc = []
    for i in L:
        Lc += [int(i)]
    return trie(Lc)

L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
print(float_to_int_to_trie(L))