import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.optimize import curve_fit, minimize
from scipy import signal, fftpack, linalg

#x = np.linspace(0, 10, 10) # création d'un tableau de 100 points entre 0 et 10
#y = x**2

#f = interp1d(x, y, kind='linear') # création d'une fonction d'interpolation linéaire
#x_new = np.linspace(0, 10, 30) # création d'un tableau de 30 points entre 0 et 10
#y_new = f(x_new) # évaluation de la fonction d'interpolation


#plt.scatter(x, y) # création d'un graphique de dispersion
#plt.scatter(x_new, y_new, color='red') # ajout des points interpolés en rouge
#plt.show() # affichage du graphique

# curve fitting
#x = np.linspace(0, 2, 100) # création d'un tableau de 100 points entre 0 et 10
#y = 1/3*x**3 - 3/5 * x**2 + 2 + np.random.randn(x.shape[0])/20 

#def model(x, a, b, c):
   # return a*x**3 + b*x**2 + c

#popt, pcov = curve_fit(model, x, y) # ajustement de la fonction modèle aux données, popt contient les paramètres optimaux

#print("Paramètres optimaux : ", popt)
#y_fit = model(x, *popt) # évaluation de la fonction ajustée avec les paramètres optimaux

#plt.scatter(x, y) # création d'un graphique de dispersion
#plt.plot(x, y_fit, color='red') # ajout de la courbe ajustée en rouge
#plt.show() # affichage du graphique

# minimization
#def objective(x):
   # return x**2 + 15 + 15*np.sin(x) # définition de la fonction objective à minimiser

#result = minimize(objective, x0=0) # minimisation de la fonction objective avec un point de départ x0=0
#plt.plot(np.linspace(-10, 10, 100), objective(np.linspace(-10, 10, 100))) # tracé de la fonction objective
#plt.scatter(result.x, result.fun, color='red') # ajout du point minimum trouvé en rouge
#plt.show() # affichage du graphique
#print("Minimum trouvé en : ", result.x)

# signal processing
#t = np.linspace(0, 1, 1000) # création d'un tableau de 1000 points entre 0 et 1
#signal1 = np.sin(2*np.pi*5*t) # signal de fréquence 5 Hz
#signal2 = np.sin(2*np.pi*20*t) # signal de fréquence 20 Hz
#signal3 = 3*np.sin(2*np.pi*50*t) # signal de fréquence 50 Hz
#signal_mixed = signal1 + signal2 + signal3 # mélange des trois signaux
#frequencies, power = signal.periodogram(signal_mixed , fs=1000) # calcul du spectre de puissance du signal mélangé
#plt.plot(frequencies, power) # tracé du spectre de puissance
#plt.show() # affichage du graphique

#application of fourier transform
#x = np.linspace(0, 30, 1000) # création d'un tableau de 1000 points entre 0 et 1
#y = 3*np.sin(x) + 2*np.sin(5*x) + np.sin(10*x) + np.random.randn(x.shape[0]) # signal composé de trois sinusoïdes plus du bruit
#plt.figure(figsize=(10, 6)) # création d'une figure de taille 10x6 pouces
#plt.subplot(2, 1, 1) # création d'un sous-graphe
#plt.plot(x, y) # tracé du signal

#frequencies, powwer = signal.periodogram(y) # calcul du spectre de puissance du signal
#powwer[powwer < 400] = 0 # filtrage du spectre de puissance pour ne garder que les composantes inférieures à 100

# Inverse Fourier Transform en utilisant le nouveau spectre de puissance filtré
#y_filtered = fftpack.irfft(powwer) # calcul du signal filtré à partir du spectre de puissance filtré
#x_filtered = fftpack.rfftfreq(frequencies) # création d'un tableau de points pour le signal filtré
#plt.subplot(2, 1, 1) # création d'un sous-graphe
#plt.plot(x_filtered, y_filtered, color='blue') # tracé du signal filtré    
#plt.show() # affichage du graphique

# création d'un dataset contenant la tailles des bactéries contenue dans un image grace à ndimage
from scipy import ndimage
# importer une image et la convertir en un tableau numpy

image = plt.imread('bacteria_image.png') # remplacer 'bacteria_image.png' par le chemin de votre image
image = np.mean(image, axis=2) # conversion de l'image en niveaux de gris
ravelled_image = image.flatten() # aplatir l'image en un tableau 1D
histogram, bin_edges = np.histogram(ravelled_image, bins=256) # calcul de l'histogramme de l'image
plt.plot(bin_edges[:-1], histogram) # tracé de l'histogramme
# étiquetage des régions de l'image où les valeurs sont supérieures à 0.5
labeled_image, num_features = ndimage.label(image > 0.5) # étiquetage des régions de l'image où les valeurs sont supérieures à 0.5
print("Nombre de régions détectées : ", num_features)
