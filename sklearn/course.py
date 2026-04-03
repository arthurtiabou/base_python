from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

np.random.seed(0)
m = 100
X = np.linspace(0, 10, m).reshape(m, 1)
y = X**2 + np.random.randn(m, 1)

#model = LinearRegression()
model = SVR()

model.fit(X, y)

score = model.score(X, y)
print(f"R^2 Score: {score}")

#plt.scatter(X, y)
#plt.plot(X, model.predict(X), color='red', label='Regression Line')
#plt.show()

# model de classification

titanic = pd.read_excel('./dataset/titanic.xls')
titanic = titanic[['survived', 'pclass', 'sex', 'age']]
titanic.dropna(axis=0, inplace=True)
titanic['sex'] = titanic['sex'].replace(['male', 'female'], [0, 1])

print(titanic.head())

Y = titanic['survived']
X = titanic.drop('survived', axis=1)

model = KNeighborsClassifier()

model.fit(X, Y)

score = model.score(X, Y)
print(f"Accuracy: {score}")

predictions = model.predict(X[:5])

def survival_probability(model, pclass , sex, age):
    X_new = np.array([[pclass, sex, age]]).reshape(1, 3)
    prediction = model.predict(X_new)
    if prediction[0] == 1:
        return "Survived"
    else:
        return "Did not survive"
    

print(survival_probability(model, 1, 0, 23)) # Classe 1, homme, 30 ans