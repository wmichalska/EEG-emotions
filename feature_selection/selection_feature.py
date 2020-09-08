from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import pandas as pd

#file before inputation
data_raw = pd.read_csv("../structured_features_deleted_nan_to_0.csv")

#file after change nan values into mean
# data_imputed = pd.read_csv("imputed2.csv")

#treshold value
sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
# sel = VarianceThreshold(threshold=0.2)

selected_raw = sel.fit_transform(data_raw)
selected_rows = sel.get_support()

# selected = sel.fit_transform(data_imputed)

print("Size of raw table without selection = ", data_raw.shape)

print("Size of raw table with selection = ", selected_raw.shape)

# print("Size of inputed table after feature selection = ", selected.shape)

print(selected_rows)
print('end')