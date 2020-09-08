from sklearn.neighbors import NearestCentroid
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.multioutput import MultiOutputClassifier
from sklearn.neighbors import KNeighborsClassifier

features_raw = pd.read_csv('nine_without.csv')
valence_raw = pd.read_csv('nine_emotions.csv')

features = np.array(features_raw)
valence = np.array(valence_raw)

valence_train_rows = valence[30:299, :]
train_rows = features[30:299, :]
true_features = features[0:30, :]
true_valence = valence[0:30, :]

# clf = NearestCentroid()
# knn = NearestCentroid()
clf = NearestCentroid()
clf = clf.fit(train_rows, valence_train_rows)
result = clf.predict(true_features)

y_pred = result
y_true = true_valence


a = accuracy_score(y_true, y_pred)
from sklearn.metrics import cohen_kappa_score

b = cohen_kappa_score(y_true, y_pred)
from sklearn.metrics import confusion_matrix
c = confusion_matrix(y_true, y_pred)
from sklearn.metrics import hamming_loss
d = hamming_loss(y_true, y_pred)
print('end')