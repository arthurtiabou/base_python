import numpy as np

np.random.seed(0) # pour la reproductibilité des résultats
A = np.random.randint(0, 100, (10, 5)) # création
mv = np.mean(A, axis=0) # calcul de la moyenne de chaque colonne
ev = np.std(A, axis=0) # calcul de l'écart-type de chaque colonne

A =  (A - mv) / ev # centrage et réduction des données en soustrayant la moyenne et en divisant par l'écart-type de chaque colonne

print(np.mean(A, axis=0)) # vérifie que la moyenne de chaque colonne est maintenant 0
print(np.std(A, axis=0)) # vérifie que l'écart-type de chaque

print(A) # vérifie que les données ont été centrées et réduites correctement   