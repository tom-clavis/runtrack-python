def fonction_jardin(type,saison):
    
    if type == "fruit" and saison == "hiver":
        print("orange, mandarine, kiwi")
        
    elif type == "fruit" and saison == "été":
        print("Poire, fraise, cassis")
        
    elif type == "legume" and saison == "hiver":
        print("carrote, topinambour, endive")
        
    elif type == "legume" and saison == "été":
        print("artichaut, aubergine, navet")
        
    
fonction_jardin("fruit","hiver")
fonction_jardin("legume","hiver")
fonction_jardin("fruit","été")
fonction_jardin("legume","été")