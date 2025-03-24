
def nomMois(n):
    # renvoie le nom du nième mois de l'année
    mois = ['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre','Octobre','Novembre','Décembre']
    if (n < 12):
        return mois[(n-1)]

print(nomMois(4))

def inverse(ch):
    # inverse l'ordre des caractères d'une chaîne quelconque
    inversed = ""
    indice = 0
    while(indice < len(ch)):
        inversed = ch[indice] + inversed
        indice += 1
    return inversed

print(inverse("polynôme"))

def compteMots(ph):
    # renvoie le nombre de mots contenus dans la phrase ph
    nbEspaces = 0
    indice  = 0
    # Il faudrait au préalable supprimer les espaces au début de la phrase et les espaces à la fin de la phrase
    # De même il faudrait traiter les espaces successifs
    while(indice < len(ph)):
        if( ph[indice] == " "):
            nbEspaces += 1
        indice += 1
    return (nbEspaces+1)

print(compteMots("Bozo est le meilleur de tous."))