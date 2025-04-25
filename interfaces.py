# Dans l'exemple qui suit nous allons créer une fenêtre très simple et y ajouter 
# deux widgets typiques: un bout de texte (Label) et un bouton (Button)
from tkinter import *  # importons toutes les classes contenues dans le module tkinter
# Nous utilisons une des classes du module tkinter, la classe Tk() et nous en créons une instance
# une instance est un objet spécifique
# C'est la méthode d'instanciation d'un objet à partir d'une classe
# La classe est un modèle général (ou un moule) à partir duquel on demande à la machine de construire
# un objet informatique particulier
# La classe Tk(), qui est l'une des classes les plus fondamentales de la bibliothèque tkinter,
# contient tout ce qu'il faut pour engendrer différentes types de fenêtres d'application, de tailles ou de couleurs
# diverses, avec ou sans barre de menus.
# Nous nous en servons ici pour créer notre objet graphique de base, à savoir la fenêtre qui contiendra tout le reste.
# L'instruction d'instanciation ressemble à une simple affectation de variable. Comprenons bien cependant qu'il se passe
# ici deux choses à la fois:
# - La création d'un nouvel objet
# - L'affectation d'une variable qui va désormais servir de référence pour manipuler cet objet.
fen1 = Tk() # Cette concision du langage est une conséquence du typage dynamique des variables en python

tex1 = Label(fen1, text='Bonjour tout le monde !', fg = 'red')# fg = foreground (couleur d'avant-plan)
# La classe Label() définit toute sorte d'étiquettes (ou de libellés). En fait, il s'agit tout simplement de fragments
# de texte quelconques, utilisables pour afficher des informations et des messages divers à l'intérieur d'une fenêtre.
# Nous créons ici l'objet text1 par instanciation de la classe Label()
# Le premier argument passé à l'instanciation (fen1) indique que le nouveau widget (=composant graphique) que nous sommes
# en train de créer sera contenu dans un autre widget préexistant que nous désignons ici comme son maître:
# l'objet fen1 est le widget maître de l'objet tex1


tex1.pack()
# La méthode pack() réduit automatiquement la taille de la fenêtre "maître" afin qu'elle soit juste assez grande pour contenir
# les widgets "esclaves" définis au préalable.

bou1 = Button(fen1, text='Quitter', command = fen1.destroy)
bou1.pack()
fen1.mainloop()


