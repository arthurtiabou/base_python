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