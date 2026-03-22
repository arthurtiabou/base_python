from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
from skimage import data

face = data.astronaut() 

zoom = face[127:374, 127:374] # zoom de l'image

print(face.shape) # image exemple
print(zoom.shape) # zoom de l'image
plt.imshow(face)
plt.imshow(zoom)
plt.show()