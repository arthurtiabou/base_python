import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier, StackingClassifier
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier, AdaBoostClassifier, GradientBoostingClassifier

X, y = make_moons(n_samples=500, noise=0.3, random_state=0)
#plt.scatter(X[:, 0], X[:, 1], c=y)
#plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model_1 = SGDClassifier(random_state=0)
model_2 = DecisionTreeClassifier(random_state=0)
model_3 = KNeighborsClassifier(n_neighbors=2)
model_4 = VotingClassifier(
    estimators=[("SGD", model_1), ("Tree", model_2), ("KNN", model_3)],
    voting="hard",
)

for model in (model_1, model_2, model_3, model_4):
    model.fit(X_train, y_train)
    print(f"{model.__class__.__name__} score: {model.score(X_test, y_test)}")


model_5 = BaggingClassifier(n_estimators=100)
model_5.fit(X_train, y_train)
print(f"BaggingClassifier score: {model_5.score(X_test, y_test)}")

model_6 = RandomForestClassifier(n_estimators=100)
model_6.fit(X_train, y_train)
print(f"RandomForestClassifier score: {model_6.score(X_test, y_test)}")


model_7 = AdaBoostClassifier(n_estimators=100)
model_7.fit(X_train, y_train)
print(f"AdaBoostClassifier score: {model_7.score(X_test, y_test)}")

model_8 = GradientBoostingClassifier(n_estimators=100)
model_8.fit(X_train, y_train)
print(f"GradientBoostingClassifier score: {model_8.score(X_test, y_test)}")

model_9 = StackingClassifier(
    estimators=[("SGD", model_1), ("Tree", model_2), ("KNN", model_3)],
    final_estimator=KNeighborsClassifier(),
)
model_9.fit(X_train, y_train)
print(f"StackingClassifier score: {model_9.score(X_test, y_test)}")