from sklearn.neighbors import NearestCentroid
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import AdaBoostClassifier

features_raw = pd.read_csv("nine_without.csv")
valence_raw = pd.read_csv("nine_emotions.csv")

features = np.array(features_raw)
valence = np.array(valence_raw)

valence_train_rows = np.ravel((valence[30:299, :]))
train_rows = features[30:299, :]
true_features = features[0:30, :]
true_valence = valence[0:30, :]

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