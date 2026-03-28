import math
import random
import statistics
import os
import glob


print(math.pi)
print(random.randint(1, 10))
data = [1, 2, 3, 4, 5]
print(random.choice(data)) # Affiche un élément aléatoire de la liste data
print(random.sample(data, 3)) # Affiche une liste de 3 éléments aléatoires de data
print(statistics.mean(data))
print(statistics.median(data))# Affiche la médiane de data, qui est 3
print(statistics.mode(data))# Affiche la valeur la plus fréquente dans data, qui est 1, 2, 3, 4 ou 5 (tous ont la même fréquence)

print(os.getcwd()) # Affiche le répertoire de travail actuel
print(glob.glob("*.txt")) # Affiche une liste de tous les fichiers .txt dans le répertoire actuel