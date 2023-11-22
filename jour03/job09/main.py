def moyenne(note1, note2, note3):
    return (note1 + note2 + note3)/3

n1 = int(input("1er note :"))
n2 = int(input("2ème note :"))
n3 = int(input("3ème note :"))
moyenne_etudiant = moyenne(n1,n2,n3)

if  15 <= moyenne_etudiant <=20:
    print(f"Moyenne : {moyenne_etudiant} \n Tres bon élève")
elif  11 <= moyenne_etudiant <=14:
    print(f"Moyenne : {moyenne_etudiant} \n Bon élève")
elif  8 <= moyenne_etudiant <=10:
    print(f"Moyenne : {moyenne_etudiant} \n Elève moyen")
if  0 <= moyenne_etudiant <= 7:
    print(f"Moyenne : {moyenne_etudiant} \n Elève devant faire des efforts")   