import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2, 10) # création d'un vecteur de 10 points entre 0 et 2
y = 3*x + 5 # calcul de la fonction cube pour chaque élément de x

plt.figure() # création d'une nouvelle figure
# utilisation de subplots pour créer une grille de 1 ligne et 2 colonnes, et sélectionner la première colonne pour le tracé
plt.subplot(2, 3, 1)
plt.plot(x, y, label = 'fonction affine') # tracé de la courbe de y en fonction de x

plt.subplot(2, 3, 2)
plt.plot(x, x**2, label = 'parabole', marker = 'o') # ajout de points rouges sur la courbe
plt.xlabel('abscisses') # étiquette de l'axe des x
plt.ylabel('ordonnées') # étiquette de l'axe des y
plt.legend() # affichage de la légende
plt.show() # affichage du graphique