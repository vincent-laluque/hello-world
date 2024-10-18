# un grand nombre de secondes
nombre = 12345678912

# Sous python3, l'opérateur de division / effectue une division réelle. Si vous souhaitez obtenir une division entière, 
# vous devez utiliser l'opérateur //
years = nombre//(365*24*3600)
print(years)

secondesquirestent = nombre%(365*24*3600)
print(secondesquirestent)

mois = secondesquirestent//(30*24*3600)
print(mois)

secondesquirestent = secondesquirestent%(30*24*3600)
jours = secondesquirestent//(24*3600)
print(jours)

secondesquirestent = secondesquirestent%(24*3600)
print(secondesquirestent)

heures = secondesquirestent//(3600)
print(heures)

secondesquirestent = secondesquirestent%(3600)
print(secondesquirestent)

minutes = secondesquirestent//60
print(minutes)

secondes = secondesquirestent%(60)
print(secondes)

print( years,"ans", mois,"mois",jours, "jours", heures, "heures", minutes,"minutes",secondes,"secondes",sep=" ")


# nombre de secondes fournies au départ:
nsd  = 12345678912

# nombre de secondes dans une journée:
nspj = 3600 * 24

# nombre de secondes dans un an (=365 jours) 
# on ne tiendra pas compte des années bissextiles
nspa = nspj * 365

# nombre de secondes dans un mois (en admettant pour chaque mois une durée identique de 30 jours)
nspm = nspj * 30

# nombre d'années contenues dans la durée fournie:
na = nsd // nspa

# nombre de secondes restantes:
nsr = nsd % nspa

# nombre de mois restants:
nmo = nsr // nspm

# nombre de secondes restantes:
nsr = nsr % nspm

# nombre de jours restants:
nj = nsr // nspj

# nombre de secondes restantes:
nsr = nsr % nspj

# nombre d'heures restantes:
nh = nsr // 3600

# nombre de secondes restantes:
nsr = nsr % 3600

#nombre de minutes restantes:
nm = nsr // 60

# nombre de secondes restantes:
nsr = nsr % 60


print("Nombre de secondes à convertir: ", nsd)
print("Cette durée correspond à", na, "année de 365 jours, plus")
print(nmo,"mois de 30 jours,",end=' ')
print(nj,"jours,",end='')
print(nh,"heures,",end='')
print(nm,"minutes et,",end='')
print(nsr,"secondes.")












