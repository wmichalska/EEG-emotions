import numpy as np
from sklearn.impute import SimpleImputer
import pandas as pd
from sklearn.impute import SimpleImputer

dataFrame = pd.read_csv("structured_features.csv")

imp = SimpleImputer(strategy="most_frequent")
print(imp.fit_transform(dataFrame))

a = np.asarray(imp.fit_transform(dataFrame))
np.savetxt("imputed2.csv", a, delimiter=",")

print('dd')
