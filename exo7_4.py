# ecrire une fonction qui retourne le volume d'une boite parallélépipédique dont on fournit les trois dimensions en argument

def volBoite(x1,x2,x3):
    "Volume d'une boîte parallélipédique"
    return x1*x2*x3

print(round(volBoite(5.2, 7.7, 3.3),3))
