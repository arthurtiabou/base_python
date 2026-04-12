from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs, load_digits
from sklearn.ensemble import IsolationForest
from sklearn.decomposition import PCA

import numpy as np

X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

model = KMeans(n_clusters=3)
model.fit(X)
model.predict([[0, 0], [4, 4]])
#plt.scatter(X[:, 0], X[:, 1], c=model.labels_, cmap='viridis')
#plt.show()

inertia = []
K_range = range(1, 20)

for k in K_range:
    model = KMeans(n_clusters=k)
    model.fit(X)
    inertia.append(model.inertia_)

#plt.plot(K_range, inertia, 'bx-')
#plt.xlabel('k')
#plt.ylabel('Inertia')
#plt.title('Elbow Method For Optimal k')
#plt.show()

# Détection d'anomalies
model = IsolationForest(contamination=0.05)
model.fit(X)
anomalies = model.predict(X)
#plt.scatter(X[:, 0], X[:, 1], c=anomalies, cmap='coolwarm')
#plt.title('Anomaly Detection with Isolation Forest')
#plt.show()

digits = load_digits()
images = digits.images
X = digits.data
y = digits.target

model = IsolationForest(random_state=0, contamination=0.02)
model.fit(X)
anomalies = model.predict(X)
#plt.scatter(X[:, 0], X[:, 1], c=anomalies, cmap='coolwarm')
#plt.title('Anomaly Detection on Digits Dataset')   
#plt.show()

# Réduction de dimensionnalité pour visualiser les anomalies

model = PCA(n_components=64)
X_reduced = model.fit_transform(X)
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y)
plt.title('Anomaly Detection on Digits Dataset (PCA)')
plt.show()