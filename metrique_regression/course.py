import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import *

y = np.array([1, 2])
y_pred = np.array([1, 3])

print('MAE:', mean_absolute_error(y, y_pred))
print('MSE:', mean_squared_error(y, y_pred))
print('RMSE:', np.sqrt(mean_squared_error(y, y_pred)))
print('R²:', r2_score(y, y_pred))