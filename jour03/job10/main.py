def fonction_pair_impair(nombre):
    if nombre < 0 or type(nombre)!=int:
        print("Le nombre n'est pas positif ou un entier")
    else:
        if nombre%2 == 0:
            print(f"Le nombre {nombre} est pair")
        else:
            print(f"Le nombre {nombre} est impair")

fonction_pair_impair(1)
fonction_pair_impair(2)
fonction_pair_impair(-1.3)