from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.svm import LinearSVC
from sklearn.pipeline import make_pipeline
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree
import pandas as pd
import random
from sklearn import metrics
from sklearn.metrics import jaccard_score

features_raw = pd.read_csv('feautery_274.csv', header=None)
features = np.array(features_raw)
valence_raw = pd.read_csv('emocje_274.csv', header=None)
valence = np.array(valence_raw)
valence_ravel = np.array(np.ravel(valence_raw))

# E = np.random.RandomState(42).uniform(0, 0.1, size=(X.shape[0], 20))
# X1 = np.hstack((features, E))
X = preprocessing.MinMaxScaler().fit_transform(features)

y = valence_ravel

y_train = (valence[32:, :])
X_train = X[32:, :]

X_test = X[:32, :]
y_test = valence[:32, :]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)

# clf.predict(X_test)
# clf.predict_proba(X_test)
result = clf.predict(X_test)

y_pred = result

# print(len(y_pred['AWE']))

a = accuracy_score(y_test, y_pred)
y_true = y_test

# fig, ax = plt.subplots(figsize=(10, 10))  # whatever size you want
# tree.plot_tree(clf, ax=ax, max_depth=4, fontsize=6)
# plt.savefig('tree_high_dpi', dpi=100)
# plt.show()
# plt.savefig('tree_high_dpi', dpi=100)
from sklearn import metrics
from sklearn.metrics import jaccard_score
precision_score=metrics.precision_score(y_true, y_pred, average='macro')

recall_score=metrics.recall_score(y_true, y_pred, average='micro')

f1_score=metrics.f1_score(y_true, y_pred, average='weighted')

f1_score2=metrics.f1_score(y_true, y_pred, average='micro')

f1_score3=metrics.f1_score(y_true, y_pred, average='macro')



fbeta_score=metrics.fbeta_score(y_true, y_pred, average='macro', beta=0.7)

precision_recall_fscore_support=metrics.precision_recall_fscore_support(y_true, y_pred, beta=0.5, average=None)

print(y_pred)

print('d')
