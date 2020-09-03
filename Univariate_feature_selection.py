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

features_raw = pd.read_csv("structured_features_deleted_nan_to_0.csv")
features = np.array(features_raw)
valence_raw = pd.read_csv('valence_values.csv')
valence = np.array(valence_raw)
valence_ravel = np.array(np.ravel(valence_raw))

# E = np.random.RandomState(42).uniform(0, 0.1, size=(X.shape[0], 20))
# X1 = np.hstack((features, E))
X = preprocessing.MinMaxScaler().fit_transform(features)

y=valence_ravel

y_train = (valence[56:451, :])
X_train = X[56:451, :]

X_test = X[0:56, :]
y_test = valence[0:56, :]

# X_train, X_test, y_train, y_test = train_test_split(
#         X, y, stratify=y, random_state=0
# )


X_indices = np.arange(X.shape[-1])

print(X.shape)

selector = SelectKBest(chi2, k=10)
selector.fit_transform(X, y.ravel())




# scores = -np.log10(selector.pvalues_)
# scores /= scores.max()
# plt.bar(X_indices - .45, scores, width=.2,
#         label=r'Univariate score ($-Log(p_{value})$)')

# Compare to the weights of an SVM
clf = make_pipeline(MinMaxScaler(), LinearSVC())
clf.fit(X_train, y_train)
print('Classification accuracy without selecting features: {:.3f}'
      .format(clf.score(X_test, y_test)))

svm_weights = np.abs(clf[-1].coef_).sum(axis=0)
svm_weights /= svm_weights.sum()

plt.bar(X_indices - .25, svm_weights, width=.2, label='SVM weight')

clf_selected = make_pipeline(
        SelectKBest(f_classif, k=10), MinMaxScaler(), LinearSVC()
)
clf_selected.fit(X_train, y_train)
print('Classification accuracy after univariate feature selection: {:.3f}'
      .format(clf_selected.score(X_test, y_test)))

svm_weights_selected = np.abs(clf_selected[-1].coef_).sum(axis=0)
svm_weights_selected /= svm_weights_selected.sum()

plt.bar(X_indices[selector.get_support()] - .05, svm_weights_selected,
        width=.2, label='SVM weights after selection')


plt.title("Comparing feature selection for 10 best features")
plt.xlabel('Feature number')
plt.yticks(())
plt.axis('tight')
plt.legend(loc='upper right')
plt.show()




print('shape')
