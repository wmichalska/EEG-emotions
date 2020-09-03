from sklearn import svm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


features_raw = pd.read_csv("structured_features_deleted_nan_to_0.csv")
valence_raw = pd.read_csv('valence_values.csv')

features = np.array(features_raw)
valence = np.array(valence_raw)

valence_train_rows = valence[56:451, :]
train_rows = features[56:451, :]
true_features = features[0:56, :]
true_valence = valence[0:56, :]

from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn import svm

clf = svm.SVC()

C = 1.0  # SVM regularization parameter
# clf = svm.SVC(kernel='linear', C=C)
# clf = svm.LinearSVC(C=C, max_iter=10000
# clf = svm.SVC(kernel='rbf', gamma=0.7, C=C)
# clf = svm.SVC(kernel='poly', degree=3, gamma='auto', C=C)

# clf = tree.DecisionTreeClassifier()
clf = clf.fit(train_rows, valence_train_rows)
result = clf.predict(true_features)

print("True = ",true_valence)
print("Estimated = ", result)

y_pred = result
y_true = true_valence

# get support vectors
g = clf.support_vectors_


# get indices of support vectors
f = clf.support_

# get number of support vectors for each class
d = clf.n_support_

a = accuracy_score(y_true, y_pred)

# b = accuracy_score(y_true, y_pred, normalize=True)




print("done")
