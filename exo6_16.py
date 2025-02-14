# Ecrire un script qui affiche la valeur de la force de gravitation s'exerçant entre deux masses de 10 000 kg,
# pour des distances qui augmentent suivant une progression géométrique de raison 2, à partir de 5 cm (0,05 mdistance)

# importer un module de fonctions:
from math import * 

masse1 = 10000
masse2 = 10000

distance = 0.05

# Constante de gravitation (pour qu'une donnée numérique soit considérée par Python comme étant du type float,
# il suffit qu'elle contienne dans sa formulation un élément tel qu'un point décimal ou un exposant de 10)

consGravitation = 6.67e-11 

step = 1
while (step < 5):
    laForce = consGravitation*(masse1*masse2)/(distance*distance)
    print("d = ",distance," m : la force vaut", round(laForce,4)," N")
    distance *= 2
    step += 1


