import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.metrics import *
from sklearn.pipeline import make_pipeline, make_union
from sklearn.preprocessing import *
from sklearn.linear_model import SGDClassifier
from sklearn.compose import make_column_transformer, make_column_selector
import seaborn as sns


titanic = sns.load_dataset('titanic')

transformer = make_column_transformer((StandardScaler(), ['age', 'fare']))

y = titanic['survived']
X = titanic.drop(['survived'], axis=1)

print(X.head())

#numerical_features = ['pclass', 'age', 'fare']
#categorical_features = ['sex', 'deck', 'alone']
numerical_features = make_column_selector(dtype_include=np.number)
categorical_features = make_column_selector(dtype_include=object)

numerical_pipeline = make_pipeline(SimpleImputer(), StandardScaler())
categorical_pipeline = make_pipeline(SimpleImputer(strategy='most_frequent'), OneHotEncoder(handle_unknown='ignore'))

preprocessor = make_column_transformer((numerical_pipeline, numerical_features), (categorical_pipeline, categorical_features))

model = make_pipeline(preprocessor, SGDClassifier())
model.fit(X, y)

# Pipeline parallèle

pipeline = make_union(StandardScaler(), Binarizer())
pipeline.fit_transform(numerical_features)
print(pipeline.transform(numerical_features).shape)


