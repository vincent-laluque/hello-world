# Ce fichier est un module de fonction python
from turtle import *

def carre(taille, couleur):
    "fonction qui dessine un carré de taille et de couleur déterminées"
    color(couleur)
    c = 0
    while c < 4:
        forward(taille)
        right(90)
        c += 1

def carreAngle(taille,couleur,angle):
    color(couleur)
    left(angle)
    c = 0
    while c < 4:
        forward(taille)
        right(90)
        c += 1

def triangle(taille, couleur, angle):
    color(couleur)
    left(angle)
    c = 0
    while c < 3:
        forward(taille)
        right(120)
        c += 1

def etoile5(taille, couleur, angle):
    color(couleur)
    left(angle)
    c = 0
    while c < 5:
        forward(taille)
        right(144)
        c += 1
