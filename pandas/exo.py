import pandas as pd
import numpy as np

data = pd.read_excel('./dataset/titanic.xls') # lecture d'un fichier Excel contenant des données
data = data.drop(['name', 'ticket', 'cabin', 'body', 'boat', 'embarked', 'fare', 'parch', 'sibsp', 'home.dest'], axis=1) # suppression de certaines colonnes du DataFrame

bins = [0, 20, 30, 40, float('inf')]
labels = [0, 1, 2, 3]

data['age'] = pd.cut(data['age'], bins=bins, labels=labels)

print(data.head()) # affichage des 5 premières lignes du DataFrame après remplacement des âges