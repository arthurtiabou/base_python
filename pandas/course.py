import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel('./dataset/titanic.xls') # lecture d'un fichier Excel contenant des données
print(data.head()) # affichage des 5 premières lignes du DataFrame
print(data.shape) # affichage de la forme du DataFrame (nombre de lignes et de colonnes)

data = data.drop(['name', 'ticket', 'cabin', 'body', 'boat', 'embarked', 'fare', 'parch', 'sibsp', 'home.dest'], axis=1) # suppression de certaines colonnes du DataFrame
print(data.head()) # affichage des 5 premières lignes du DataFrame après suppression de certaines colonnes
print(data.describe()) # affichage de statistiques descriptives sur les données numériques du DataFrame

data = data.dropna(axis = 0) # suppression des lignes contenant des valeurs manquantes
print(data.shape)

print(data.iloc[0:2, :]) # affichage des 2 premières lignes du DataFrame

print(data.groupby(['sex' , 'pclass']).mean()) # calcul de la moyenne de chaque groupe de sexe

plt.scatter(data['age'], data['survived']) # création d'un graphique de dispersion entre l'âge et la survie
plt.show() # affichage du graphique