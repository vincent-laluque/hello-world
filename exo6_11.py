# Demandez à l'utilisateur d'entrer trois longueurs a, b et c
print("Veuillez entrer les longueurs des trois côtés du triangle (séparés par des virgules): ")
ch = input()
cotes = list(eval(ch))

if (len(cotes) == 3):
    print("Coucou")
    k = 0
    max = cotes[0]
    while (k < 3):
        k += 1
        if (max < cotes[k]):
            max = cotes[k]
    print("Le plus grand côté est: ",max)
else:
    print("Erreur: un triangle a trois côtés")
