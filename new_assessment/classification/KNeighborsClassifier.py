from sklearn.neighbors import NearestCentroid
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.multioutput import MultiOutputClassifier
from sklearn.neighbors import KNeighborsClassifier

features_raw = pd.read_csv('feautery_274.csv', header=None)
valence_raw = pd.read_csv('emocje_274.csv', header=None)

features = np.array(features_raw)
valence = np.array(valence_raw)

valence_train_rows = valence[32:, :]
train_rows = features[32:, :]
true_features = features[:32, :]
true_valence = valence[:32, :]

# clf = NearestCentroid()
knn = KNeighborsClassifier(n_neighbors=5)
clf = MultiOutputClassifier(knn, n_jobs=None)
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

from sklearn import metrics
from sklearn.metrics import jaccard_score
precision_score=metrics.precision_score(y_true, y_pred, average='macro')

recall_score=metrics.recall_score(y_true, y_pred, average='micro')

f1_score=metrics.f1_score(y_true, y_pred, average='weighted')

f1_score2=metrics.f1_score(y_true, y_pred, average='micro')


fbeta_score=metrics.fbeta_score(y_true, y_pred, average='macro', beta=0.7)

precision_recall_fscore_support=metrics.precision_recall_fscore_support(y_true, y_pred, beta=0.5, average=None)

print(y_pred)
precision_score2=metrics.precision_score(y_true, y_pred, average='macro')

recall_score2=metrics.recall_score(y_true, y_pred, average='micro')

f1_score2=metrics.f1_score(y_true, y_pred, average='weighted')

fbeta_score2=metrics.fbeta_score(y_true, y_pred, average='macro', beta=0.5)

precision_recall_fscore_support2=metrics.precision_recall_fscore_support(y_true, y_pred, beta=0.5, average=None)


print('end')