t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'May', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
t3 = []

indice = 1
while (indice < 13):
    t3.append(t2[indice-1])
    t3.append(t1[indice-1])
    indice = indice + 1

print(t3)

i = 0
while (i < len(t2)):
    print(t2[i], end=' ')
    i = i + 1

uneListe = [32, 5, 12, 8, 3, 75, 2, 15]

print('\n')

max = 0
i = 0

while (i < len(uneListe)):
    if (uneListe[i] > max):
        max = uneListe[i]
    i = i + 1

print("Le plus grand élément de la liste a la valeur ",max)

pairs = []
impairs = []

i = 0
while (i<len(uneListe)):
    if(uneListe[i]%2 == 0):
        pairs.append(uneListe[i])
    else:
        impairs.append(uneListe[i])
    i = i + 1

print("Les éléments pairs de la liste sont ",pairs)
print("Les éléments impairs de la liste sont ",impairs)

prenoms = ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']

courts = []
longs = []
i = 0
while (i < len(prenoms)):
    if (len(prenoms[i]) < 6):
        courts.append(prenoms[i])
    else:
        longs.append(prenoms[i])
    i = i + 1

print("Les prénoms courts sont ",courts)
print("Les prénoms longs sont ",longs)

