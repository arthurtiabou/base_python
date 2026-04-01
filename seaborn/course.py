import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# seaborn est une bibliothèque de visualisation de données basée sur matplotlib, elle permet de faire des graphiques plus jolis et plus facilement que matplotlib

#sns.function({x,y,data},{hue, size, style})
#hue: permet de différencier les points en fonction d'une variable catégorielle, par exemple la variable
titanic = sns.load_dataset('titanic')
titanic.drop(['alone', 'alive', 'who', 'adult_male', 'embark_town', 'class'], axis = 1, inplace = True)
titanic.dropna(axis = 0, inplace = True)

print(titanic.head())

#sns.boxplot(x='pclass', y='age', data=titanic, hue ='sex')
#sns.displot(titanic['fare'], kde=True) # displot pour faire un histogramme de la variable fare, kde = True pour ajouter une courbe de densité

sns.heatmap(titanic.corr()) # heatmap pour faire une carte de chaleur de la matrice de corrélation, annot = True pour afficher les valeurs de corrélation
plt.show()