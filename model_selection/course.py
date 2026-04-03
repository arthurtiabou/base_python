import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score, validation_curve, GridSearchCV, learning_curve
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier


# model_selection est une bibliothèque de scikit-learn qui permet de faire de la validation croisée, de la recherche de grille et de la courbe d'apprentissage
# validation_curve permet de faire une courbe de validation pour un hyperparamètre donné, par exemple le nombre de voisins pour un KNN, en faisant varier cet hyperparamètre et en calculant le score de l'entraînement et de la validation pour chaque valeur de cet hyperparamètre
# GridSearchCV permet de faire une recherche de grille pour trouver les meilleurs hyperparamètres pour un modèle donné, en faisant varier plusieurs hyperparamètres et en calculant le score de l'entraînement et de la validation pour chaque combinaison d'hyperparamètres
# learning_curve permet de faire une courbe d'apprentissage pour un modèle donné, en faisant varier la taille de l'échantillon d'entraînement et en calculant le score de l'entraînement et de la validation pour chaque taille d'échantillon d'entraînement

iris = load_iris()
X = iris.data
y = iris.target

print(X.shape)
#plt.scatter(X[:, 0], X[:, 1], c=y)
#plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

k = np.arange(1, 50)

train_score, val_score = validation_curve(KNeighborsClassifier(), X_train, y_train, param_name='n_neighbors', param_range=k, cv=5)

param_grid = {'n_neighbors': np.arange(1, 20), 'metric': ['euclidean', 'manhattan']}

grid = GridSearchCV(KNeighborsClassifier(), param_grid, cv=5)
grid.fit(X_train, y_train)

#print('Best parameters:', grid.best_params_)
#print('Best cross-validation score:', grid.best_score_)

model = grid.best_estimator_
#print('Test set score:', model.score(X_test, y_test))

#confussion_matrix = pd.crosstab(y_test, model.predict(X_test))
#print(confussion_matrix)

N, train_scores, val_scores = learning_curve(model, X_train, y_train, train_sizes=np.linspace(0.1, 1.0, 10), cv=5)


plt.plot(N, np.mean(train_scores, axis=1), label='Training score')
plt.plot(N, np.mean(val_scores, axis=1), label='Validation score')
plt.xlabel('Training set size')
plt.ylabel('Score')
plt.legend()
plt.show()