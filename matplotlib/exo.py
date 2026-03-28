import numpy as np
import matplotlib.pyplot as plt

dictionary = {f'experience {i}' : np.random.randn(100) for i in range(4)} # création d'un dictionnaire avec 4 expériences, chacune contenant une matrice de taille 10x5

print(dictionary['experience 0']) # vérifie le contenu du dictionnaire
plt.figure() # création d'une nouvelle figure
for i in range(4):
    plt.subplot(4, 1, i+1) # utilisation de subplots pour créer une grille de 2 lignes et 2 colonnes, et sélectionner la i-ème colonne pour le tracé
    plt.plot(dictionary[f'experience {i}'], label = f'expérience {i}') # tracé de la moyenne de chaque colonne de l'expérience i
    plt.xlabel('index des colonnes') # étiquette de l'axe des x
    plt.ylabel('moyenne') # étiquette de l'axe des y
    plt.legend() # affichage de la légende

plt.show() # affichage du graphique