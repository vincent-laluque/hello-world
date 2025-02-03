# Ecrire une boucle de programme qui demande à l'utilisateur d'entrer des notes d'élèves.
# La boucle se terminera seulement si l'utilisateur entre une note négative

clafin = False

numNotes = 0
sommeNotes = 0
uneListe = []
maxNote = 0
while (not(clafin)):
    chaine = input("Quelle est la note de cet élève ?")
    lanote = int(chaine)
    if (lanote < 0):
        clafin = True
    else:
        numNotes += 1
        sommeNotes += lanote
# Constuire progressivement une liste avec les notes entrées
        uneListe.append(lanote)
# A chaque entrée afficher le nombre de notes entrées
        print("Le nombre de notes entrées est de", numNotes)
# Afficher la note la plus élevée, la note la plus basse et la moyenne de toutes les notes
        if (lanote > maxNote):
            maxNote = lanote
        print("La note la plus élevée est", maxNote)
        if (numNotes == 1):
            minNote = uneListe[0]
        else:
            k = 1
            while (k < len(uneListe)):
                if (uneListe[k] < minNote):
                    minNote = uneListe[k]
                k += 1

        print("La note la plus basse est de ",minNote)
        print("La moyenne de toutes les notes est de ", (sommeNotes/numNotes))



        
        
