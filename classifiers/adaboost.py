from sklearn.neighbors import NearestCentroid
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import AdaBoostClassifier

features_raw = pd.read_csv("data_nan_to_0_deleted_13_viarniace.csv")
valence_raw = pd.read_csv('../valence_values.csv')

features = np.array(features_raw)
valence = np.array(valence_raw)

valence_train_rows = np.ravel((valence[56:451, :]))
train_rows = features[56:451, :]
true_features = features[0:56, :]
true_valence = valence[0:56, :]

clf = AdaBoostClassifier(n_estimators=100)
clf = clf.fit(train_rows, valence_train_rows)

scores = cross_val_score(clf, train_rows, valence_train_rows, cv=5)
scores.mean()
#
result = clf.predict(true_features)
# result2 = clf.staged_predict(true_features)

#
y_pred = result
y_true = true_valence


a = accuracy_score(y_true, y_pred)



print('e')