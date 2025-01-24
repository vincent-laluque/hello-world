# Ecrire un programme qui étant donné deux bornes entières à et b additionne les nombres multiples
# de 3 et 5 compris entre ces deux bornes.

print("Veuillez entrer deux nombre entiers séparés par des virgules: ")
ch = input()
# L'association des fonctions eval() et list() permet de convertir 
# en liste toute chaine de valeurs séparées par des virgules:
bornes = list(eval(ch))

inf = bornes[0]
sup = bornes[1]

if (sup < inf):
    sup = bornes[0]
    inf = bornes[1]

somme3et5 = 0
index = inf
while (index < sup):
    multipledetrois = ((index%3)==0)
    multipledecinq = ((index%5)==0)
    if (multipledetrois) & (multipledecinq):
        somme3et5 += index
    index += 1

print("L'addition des multiples de 3 et 5 entre ",inf, " et ", sup," est: ",somme3et5)

somme3ou5 = 0
index = inf
while (index < sup):
    multipledetrois = ((index%3)==0)
    multipledecinq = ((index%5)==0)
    if (multipledetrois) or (multipledecinq):
        somme3ou5 += index
    index += 1

print("L'addition des multiples de 3 ou 5 entre ",inf, " et ", sup," est: ",somme3ou5)
