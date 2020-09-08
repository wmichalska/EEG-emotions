#importing libraries
from sklearn.datasets import load_boston
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE
from sklearn.linear_model import RidgeCV, LassoCV, Ridge, Lasso
from sklearn.preprocessing import MinMaxScaler

features_raw = pd.read_csv("../structured_features_deleted_nan_to_0.csv")
features = np.array(features_raw)
valence_raw = pd.read_csv('../valence_values.csv')
valence = np.array(valence_raw)
valence_ravel = np.array(np.ravel(valence_raw))

# E = np.random.RandomState(42).uniform(0, 0.1, size=(X.shape[0], 20))
# X1 = np.hstack((features, E))
y = MinMaxScaler().fit_transform(valence)

X = features
# y=valence_ravel

y_train = (valence[56:451, :])
X_train = X[56:451, :]

X_test = X[0:56, :]
y_test = valence[0:56, :]

reg = LassoCV()
reg.fit(X, y)

plt.figure(figsize=(12,10))
cor = df.corr()
sns.heatmap(cor, annot=True, cmap=plt.cm.Reds)
plt.show()

print("Best alpha using built-in LassoCV: %f" % reg.alpha_)
print("Best score using built-in LassoCV: %f" %reg.score(X,y))
coef = pd.Series(reg.coef_, index = X.columns)

print("Lasso picked " + str(sum(coef != 0)) + " variables and eliminated the other " +  str(sum(coef == 0)) + " variables")

imp_coef = coef.sort_values()
import matplotlib
matplotlib.rcParams['figure.figsize'] = (8.0, 10.0)
imp_coef.plot(kind = "barh")
plt.title("Feature importance using Lasso Model")

print('end')