import numpy as np

np.random.seed(0) # pour la reproductibilité des résultats
A = np.random.randint(0, 10, (2, 3)) # création d'une matrice aléatoire de taille 2x3
print(A)

print(A.sum(axis=0)) # vérifie si au moins un élément de A est différent de zéro
print(A.sum(axis=1)) # vérifie si au moins un élément de A est différent de zéro
print(A.mean(axis=0)) # vérifie si au moins un élément de A est différent de zéro
print(A.mean(axis=1)) # vérifie si au moins un élément de A est différent
print(A.var()) # vérifie si au moins un élément de A est différent de zéro
print(np.corrcoef(A)) # vérifie si au moins un élément de A est différent de zéro

B = np.random.randint(0, 10, (5, 5)) # création d'une autre matrice aléatoire de taille 5x5
B[1, 1] = np.nan # introduit une valeur manquante (NaN) dans la matrice B
B[2,3] = np.nan
print(B.mean())

# Algèbre linéaire
C = np.random.rand(2, 3) # création d'une matrice 
D = np.random.rand(3, 2) # création d'une autre matrice
print(C.dot(D)) # produit matriciel de C et D
print(np.linalg.inv(C.dot(D))) # inverse de la matrice résultante du produit matriciel de C et D