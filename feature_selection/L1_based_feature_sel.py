from sklearn.svm import LinearSVC
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectFromModel
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score


features_raw = pd.read_csv("../structured_features_deleted_nan_to_0.csv")
valence_raw = pd.read_csv('../valence_values.csv')

features = np.array(features_raw)
valence = np.array(valence_raw)

valence_train_rows = valence[56:451, :]
train_rows = features[56:451, :]
true_features = features[0:56, :]
true_valence = valence[0:56, :]

X= train_rows
y=valence_train_rows.ravel()
print(X.shape)


lsvc = LinearSVC(C=1, penalty="l1", dual=False).fit(X, y)
model = SelectFromModel(lsvc, prefit=True)
X_new = model.transform(X)
print(X_new.shape)
fff = model.get_support()
print("new",X_new.shape)

result = lsvc.predict(true_features)

print("True = ",len(true_valence))
print("Estimated = ", len(result))

y_pred = result
y_true = true_valence

a = accuracy_score(y_true, y_pred)


print(X_new.shape)