from sklearn.impute import SimpleImputer, KNNImputer, MissingIndicator
import numpy as np
from sklearn.pipeline import make_union

X = np.array([[1, 2], [np.nan, 3], [7, 6]])
imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X)
print('Imputed data:\n', X_imputed)

missing_indicator = MissingIndicator()
X_missing = missing_indicator.fit_transform(X)
print('Missing indicator:\n', X_missing)

pipeline = make_union(SimpleImputer(strategy='mean'), MissingIndicator())
