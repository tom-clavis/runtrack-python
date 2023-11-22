init_inv = 2000
rend = 1.20

def gain(somme, taux):
    total = somme * taux
    gain = total - somme
    print(f"gain : {gain}")

gain(init_inv, rend)

init_inv += 5000
rend += 0.02

gain(init_inv, rend)

init_inv *= 0.9
rend -= 0.01

gain(init_inv, rend)