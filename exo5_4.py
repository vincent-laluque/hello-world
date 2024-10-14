somme = 100

tauxFixe = 4.3 

k = 0
while k < 20 :
    k = k + 1
    interets = (somme * (tauxFixe/100))
    somme = somme + interets
    print('intérêts au bout de ',k,"an(s) :",interets," €")
