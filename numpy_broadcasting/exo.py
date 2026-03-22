import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([1, 2, 3])
B = B.reshape(1, 3) # reshape de B pour qu'il puisse être ajouté à A

print(A + B) # addition de A et B