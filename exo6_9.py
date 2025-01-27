print("Entrer une année: ", end="")
ch = input()

annee = int(ch)

bissextile = False

if ((annee % 4) == 0):
    if ((annee % 100) == 0):
        if ((annee % 400) == 0):
            bissextile = True        
        else:
            bissextile = False
    else:
        bissextile = True
else:
    bissextile = False

if (bissextile):
    print("L'année ",annee, " est une année bissextile", sep="")
else:
    print("L'année ", annee," n'est pas une année bissextile", sep="")

