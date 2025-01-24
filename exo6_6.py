a = 5
b = 2
if (a == 5) & (b <= 2):
    print('"&" signifie "et"; on peut aussi utiliser\
          le mot "and"')
    
a, b = 2, 4
if (a == 4) or ( b != 4):
    print('gagné')
elif (a == 4) or (b ==4):
    print('presque gagné')

a = 0
if not a:
    print('gagné --- ')
elif a:
    print('perdu***')