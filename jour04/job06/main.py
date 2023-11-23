def liste(L):
    last = L[0]
    L[0] = L[len(L)-1]
    L[len(L)-1] = last
    print(L)
L = [1,2,3,4,5]

liste(L)

