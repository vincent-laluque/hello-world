from sys import exit

# Demandez à l'utilisateur d'entrer trois longueurs a, b et c
print("Veuillez entrer les longueurs des trois côtés du triangle (séparés par des virgules): ")
ch = input()
cotes = list(eval(ch))

if (len(cotes) == 3):
    print("Coucou")
    indiceMax = 0
    k = 0
    max = cotes[0]
    while (k < 2):
        k += 1
        if (max < cotes[k]):
            max = cotes[k]
            indiceMax = k
    print("Le plus grand côté est: ",max)

    indiceCote1 = -1
    indiceCote2 = -1
    k = 0
    while (k < 2):
        if (indiceMax != k ):
            if (indiceCote1 == -1):
                indiceCote1 = k
            else:
                indiceCote2 = k
        k += 1

    cote1 = cotes[indiceCote1]
    cote2 = cotes[indiceCote2]

    print("La longueur du premier côté est:",cote1)
    print("La longueur du deuxième côté est:",cote2)
    longueur2cotes = cote1 + cote2
    print("La longueur des deux côtés est: ",longueur2cotes)


    if ( longueur2cotes > max):
        print("Il est possible de construire un triangle")
        if (cote1 == cote2):
            if ( max == cote1):
                print("Le triangle est équilatéral")
            else:
                if ( (cote1*cote1 + cote2*cote2) == max*max ):
                    print("Le triangle est rectangle et isocèle")
                else:
                    print("Le triangle est isocèle")
        else:
            if ( (cote1*cote1 + cote2*cote2) == max*max ):
                print("Le triangle est rectangle")
    else:
        print("Il n'est pas possible de construire un tel triangle")
        exit()

else:
    print("Erreur: un triangle a trois côtés")
