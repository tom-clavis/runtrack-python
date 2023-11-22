alphabet = "abcdefghijklmnopqrstuvwxyz"
i=0

while i < len(alphabet):
    pyra = ""
    for j in range(0,i):
        pyra += alphabet[j]
    print(pyra)
    i+=2