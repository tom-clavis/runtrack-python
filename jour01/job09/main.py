produit="pain"
prix=1
quantite=10

print("Prix initial et stock de Basse :")
print(f"{produit} : {prix} €/unité , {quantite} unité(s)")

quantite += 10
quantite -= int(input("Nombre de produit a acheter : \n"))
prix *= 1.1

print("Prix et stock augmenter :")
print(f"{produit} : {prix} €/unité , {quantite} unité(s)")