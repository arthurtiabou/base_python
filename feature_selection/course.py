import numpy as np
from sklearn.feature_selection import SelectKBest, f_classif, VarianceThreshold, chi2, SelectFromModel, RFE, RFECV
from sklearn.datasets import load_iris
from sklearn.linear_model import SGDClassifier
import matplotlib.pyplot as plt

iris = load_iris()
X, y = iris.data, iris.target

#VarianceThreshold élimine les caractéristiques dont la variance est inférieure à un seuil spécifié. Par défaut, il élimine les caractéristiques constantes (variance nulle).
print(X.var(axis=0))
selector = VarianceThreshold(threshold=0.2)
X_filtered = selector.fit_transform(X)
print(X_filtered.var(axis=0))
#plt.plot(X)
#plt.show()

#SelectKBest utilise une fonction de score pour évaluer l'importance de chaque caractéristique et sélectionne les k meilleures caractéristiques en fonction de ces scores.
selector = SelectKBest(chi2, k=2)
X_selected = selector.fit_transform(X, y)
X_support = selector.get_support()
print('Selected features:\n', X_selected)
print('Support mask:\n', X_support)

#SelectFromModel utilise un modèle d'apprentissage pour évaluer l'importance des caractéristiques et sélectionner celles qui dépassent un certain seuil.
selector = SelectFromModel(SGDClassifier(random_state=0), threshold='mean')
X_selected = selector.fit_transform(X, y)
X_support = selector.get_support()
print('Selected features:\n', X_selected)
print('Support mask:\n', X_support)

#RFE et RFECV sont des méthodes de sélection de caractéristiques récursives qui éliminent les caractéristiques les moins importantes à chaque
selector = RFECV(SGDClassifier(random_state=0), step=1, min_features_to_select=2, cv=5)
X_selected = selector.fit_transform(X, y)
X_ranking = selector.ranking_
X_scores = selector.grid_scores_
print('Selected features:\n', X_selected)
print('Feature ranking:\n', X_ranking)
print('Cross-validation scores:\n', X_scores)



