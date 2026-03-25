import numpy as np
import matplotlib.pyplot as plt

dictionary = {f'experience {i}' : np.random.randint(0, 100, (10, 5)) for i in range(1, 5)} # création d'un dictionnaire avec 4 expériences, chacune contenant une matrice de taille 10x5

print(dictionary['experience 1']) # vérifie que le dictionnaire a été créé correctement

x = np.linspace(0, 1, 10) # création d'un vecteur de 10 points entre 0 et 2

plt.figure() # création d'une nouvelle figure
for i in range(1, 5):
    plt.subplot(4, 1, i) # utilisation de subplots pour créer une grille de 2 lignes et 2 colonnes, et sélectionner la i-ème colonne pour le tracé
    plt.plot(x, dictionary[f'experience {i}'], label = f'expérience {i}') # tracé de la moyenne de chaque colonne de l'expérience i
    plt.xlabel('index des colonnes') # étiquette de l'axe des x
    plt.ylabel('moyenne') # étiquette de l'axe des y
    plt.legend() # affichage de la légende

plt.show() # affichage du graphique