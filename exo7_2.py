# Définissez une fonction lignecar(n, ca) qui renvoie une chaîne de n caractères ca

def lignecar(n, ca):
    i = 0
    chaine = ''
    while (i < n):
        chaine = chaine + ca
        i += 1
    return chaine

ca = input("Quel caractère souhaitez-vous retourner?")
n = int(input("Combien de fois souhaitez-vous retourner ce caractère?"))

chaine = lignecar(n, ca)
print(ca," * ",n," = ", chaine)


