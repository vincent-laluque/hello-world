# Comment déclarer une nouvelle liste ?
maListe = []
maListe.append('Jean-Michel')
maListe.append('Marc')
maListe.append('Vanessa')
maListe.append('Anne')
maListe.append('Maximilien')
maListe.append('Alexandre-Benoît')
maListe.append('Louise')

longueur = len(maListe)
k = 0
while ( k<longueur):
    uneLongueur = len(maListe[k])
    print(maListe[k],":",uneLongueur)
    k += 1