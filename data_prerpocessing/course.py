import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import *
from sklearn.datasets import load_iris
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV


# Etapes majeures du data preprocessing:
#encodage des variables catégorielles, imputation des valeurs manquantes, normalisation des données, sélection des caractéristiques, etc.
#Normalisation des données: permet de mettre les données sur la même échelle, ce qui est important pour certains algorithmes de machine learning, comme les KNN, les SVM, etc.
#Imputation des valeurs manquantes: permet de remplacer les valeurs manquantes par une valeur estimée, comme la moyenne, la médiane, la valeur la plus fréquente, etc.
#Sélection des caractéristiques: permet de sélectionner les caractéristiques les plus importantes pour le modèle, en utilisant des méthodes comme la sélection univariée, la sélection récursive, etc.
#Extraction de caractéristiques: permet de créer de nouvelles caractéristiques à partir des caractéristiques existantes, en utilisant des méthodes comme la PCA, la LDA, etc.

y = np.array(['chat', 'chien', 'chat', 'oiseau'])
X = np.array([['chat', 'Poils'], ['chien', 'Fourrure'], ['chat', 'Poils'], ['oiseau', 'Plumes']])

encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

print('Encoded labels:', y_encoded)

encoder2 = OneHotEncoder()
y_onehot = encoder2.fit_transform(X)
print('One-hot encoded labels:\n', y_onehot)

# Normalisation des données

X = np.array([[70], [80], [90], [100]])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print('Scaled data:\n', X_scaled)

iris = load_iris()
X = iris.data


X_minmax = MinMaxScaler().fit_transform(X)
X_robust = RobustScaler().fit_transform(X) # RobustScaler est une méthode de normalisation qui est robuste aux valeurs aberrantes, en utilisant la médiane et l'écart interquartile au lieu de la moyenne et de l'écart type pour centrer et réduire les données.

#plt.scatter(X_minmax[:, 2], X_minmax[:, 3], c=iris.target)
#plt.scatter(X_robust[:, 2], X_robust[:, 3], c=iris.target)
#plt.show()
 
# Application

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

# Normalisation des données
scaler = StandardScaler()
X_train_transformed = scaler.fit_transform(X_train)

# Estimator
model = SGDClassifier(random_state=5)
model.fit(X_train_transformed, y_train)

# Test
X_test_transformed = scaler.transform(X_test)
y_pred = model.predict(X_test_transformed)


model_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', SGDClassifier(random_state=5))
])
model_pipeline.fit(X_train, y_train)
y_pred_pipeline = model_pipeline.predict(X_test)

# utilisation de GridSearchCV pour trouver les meilleurs hyperparamètres pour le modèle

model = Pipeline([
    ('poly', PolynomialFeatures()),
    ('scaler', StandardScaler()),
    ('classifier', SGDClassifier(random_state=0))
])

params = {
    'polynomialfeatures__degree': [2, 3, 4],
    'sgdclassifier__penalty': ['l1', 'l2']
    }

grid = GridSearchCV(model, params, cv=4)

grid.fit(X_train, y_train)
print('Best parameters:', grid.best_params_)
print('Best cross-validation score:', grid.best_score_)