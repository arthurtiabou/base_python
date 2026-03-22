import numpy as np
# créer une fonction initialis

def initialisation(m,n):
    A = np.random.randn(m,n)
    B = np.ones((m,1))
    return np.concatenate((A, B), axis=1)


A = initialisation(3, 4)
print(A)