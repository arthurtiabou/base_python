import numpy as np

A =np.array([1, 2, 3])
print(A.shape)
A = A.reshape(A.shape[0], 1)
print(A.shape)
print(A)

A = A.squeeze()
print(A.shape)
print(A)

B = np.zeros((2, 3))
print(B.shape)
print(B)

C = np.ones((4, 5))
print(C.shape)

D = np.full((3, 4), 7)
print(D.shape)

E = np.eye(5)
print(E.shape)
print(E)

np.random.seed(0) # Fixe la graine pour la reproductibilité
F = np.random.randn(3, 4)
print(F)

G = np.linspace(0, 10, 5, dtype=np.float16)
print(G)

A = np.zeros((3,2))
B = np.ones((3,2))
C = np.concatenate((A, B), axis=0)
print(C)

C = C.reshape(3, 4)
print(C)
C = C.ravel()
print(C)

