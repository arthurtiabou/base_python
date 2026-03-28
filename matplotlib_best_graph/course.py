import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from mpl_toolkits.mplot3d import Axes3D


# Scatter plot des données d'entrée du dataset iris
iris = load_iris() # chargement du dataset iris
X = iris.data # données d'entrée
y = iris.target # étiquettes de classe
names = list(iris.target_names) # noms des classes

print(X.shape) # vérifie la forme des données d'entrée
print(y.shape) # vérifie la forme des étiquettes de classe

#plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', alpha = 0.7, s = 50) # tracé d'un scatter plot des deux premières dimensions des données d'entrée, coloré par les étiquettes de classe
#plt.show() # affichage du graphique

# graphique 3D des données d'entrée du dataset iris
#ax = plt.axes(projection='3d') # création d'un graphique 3D
#ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y, cmap='viridis', alpha = 0.7, s = 50) 
#plt.show() # affichage du graphique

#
#f = lambda x, y: np.sin(X) + np.cos(x+y) # définition d'une fonction à tracer
#X = np.linspace(0, 5, 100) # création d'un vecteur de 100 points entre -5 et 5   
#Y = np.linspace(0, 5, 100) # création d'un vecteur de 100 points entre -5 et 5  
#X, Y = np.meshgrid(X, Y) # création d'une grille de points à partir des vecteurs X et Y
#Z = f(X, Y) # calcul de la fonction à tracer sur la grille de points
#ax = plt.axes(projection='3d') # création d'un graphique 3D
#ax.plot_surface(X, Y, Z, cmap='viridis') # tracé de la surface de la fonction
#plt.show() # affichage du graphique

# les histogrammes

#plt.hist(X[:, 0], bins=30, alpha=0.7, label=names[0]) # tracé d'un histogramme de la première dimension des données d'entrée, avec 20 bins et une transparence de 0.7
#plt.show() # affichage du graphique

# graphique contours plot d'une fonction
f = lambda x, y: np.sin(X) + np.cos(x+y) # définition
X = np.linspace(0, 5, 100) # création d'un vecteur de 100 points entre -5 et 5
Y = np.linspace(0, 5, 100) # création d'un vecteur de 100 points entre -5 et 5
X, Y = np.meshgrid(X, Y) # création d'une grille de points à partir des vecteurs X et Y
Z = f(X, Y) # calcul de la fonction à tracer sur la grille de points
plt.contourf(X, Y, Z, 20, cmap='viridis') # tracé des contours de la fonction
plt.show() # affichage du graphique

# imshow d'une matrice
matrix = np.random.rand(10, 10) # création d'une matrice de taille 10x10 avec des valeurs aléatoires entre 0 et 1
plt.imshow(matrix, cmap='viridis') # tracé de la matrice avec imshow
plt.show() # affichage du graphique