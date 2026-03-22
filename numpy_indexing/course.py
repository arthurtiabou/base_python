import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(A)
print(A[:, 0]) # Affiche la première colonne de A
print(A[0, :]) # Affiche la première ligne de A

print(A[0:2, 0:2])
B = A[0:2, 0:2]
print(B)
C = A[:, -2:]
print(C)

B = np.zeros((4, 4))
print(B)
B[1:3, 1:3] = 1
print(B)

C = np.zeros((5, 5))
C[::2, ::2] = 1
print(C)

print(A < 5) # Affiche un tableau de booléens indiquant les éléments de A qui sont inférieurs à 5
print(A[A < 5]) # Affiche les éléments de A qui sont inférieurs à