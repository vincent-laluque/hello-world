# ecrire une fonction qui retourne le volume d'une boite parallélépipédique dont on fournit les trois dimensions en argument

def volBoite(x1,x2,x3):
    "Volume d'une boîte parallélépipédique"
    return x1*x2*x3

print(round(volBoite(5.2, 7.7, 3.3),3))

# modifier la fonction volBoite(x1,x2,x3) de manière à ce qu'elle puisse être appelée avec trois, deux, un seul ou même aucun argument

def volBoite2(x1 = 10, x2 = 10, x3 = 10):
    "Volume d'une boîte parallélépipédique"
    return x1*x2*x3

print(volBoite2())
print(volBoite2(5.2))
print(volBoite2(5.2,3))


# Vous pouvez définir une valeur par défaut pour tous les paramètres, ou une partie d'entre-eux seulement
# Dans ce cas, cependant, les paramètres sans valeurs par défaut doivent précéder les autres.

# Modifier le fonction volBoite(x1,x2,x3) de manière à ce qu'lle puisse être appelée avec un, deux ou trois arguments.
# Si un seul est utilisé, la boite est considérée comme cubique
# Si deux sont utilisés, la boite est considérée comme un prisme à base carrée
# Si trois sont utilisés, la boite est considérée comme un parallélépipède

def volBoite3(x1 = -1, x2 = -1, x3 = -1):
    if (x1 == -1):
        return -1
    else:
        if (x2 == -1):
            return x1*x1*x1
        else:
            if (x3 == -1):
                return x1*x1*x2
            else:
                return x1*x2*x3

print('-----')
print(volBoite3())
print(round(volBoite3(5.2),3))
print(round(volBoite3(5.2,3),3))
print(round(volBoite3(5.2, 3, 7.4),3))






