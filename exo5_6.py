uneChaine = "Monty python flying circus"

indice = 0
while (indice < len(uneChaine)):
    if (uneChaine[indice] == "e"):
        print("La lettre e a été trouvée à la position ",indice)
        break
    else:
        indice = indice + 1

if (indice >=len(uneChaine)):
    print("La lettre e n'a pas été trouvée dans la chaîne")


cf = "y"
indice = 0
compteur = 0
while (indice < len(uneChaine)):
    if (uneChaine[indice] == cf):
        compteur = compteur + 1
    indice = indice + 1

if (compteur == 0):
    print("La lettre", cf, "n'a pas été trouvée dans la chaîne")
else:
    print("La lettre", cf, "a été trouvée", compteur, "fois dans la chaîne")


uneChaine = "Véronique"
uneAutreChaine = ""

indice = 0
while (indice < len(uneChaine)):
    if( indice == len(uneChaine) - 1):
        uneAutreChaine = uneAutreChaine + uneChaine[indice]
    else:
        uneAutreChaine = uneAutreChaine + uneChaine[indice] + "*"
    indice = indice + 1

print(uneAutreChaine)


uneChaine = "zorglub"
uneAutreChaine = ""

indice = 0
while (indice < len(uneChaine)):
    uneAutreChaine = uneChaine[indice] + uneAutreChaine
    indice = indice + 1
    
print(uneAutreChaine)


