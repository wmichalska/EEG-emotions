# load and summarize the dataset
from pandas import read_csv
import numpy as np
from numpy import nan

# load the dataset
dataset = read_csv('../structured_features.csv', header=None)
# summarize the dataset
info = dataset.describe()
print(info)

print(dataset)

# count the number of missing values for each column
num_missing = (dataset [[0,1,2,3,4,5,6,7,8,9,10]]== 0).sum()
# report the results
print(num_missing)


# mark zero values as missing or NaN
dataset[[1,2,3,4,5]] = dataset[[1,2,3,4,5]].replace(0, nan)
# fill missing values with mean column values
dataset.fillna(dataset.mean(), inplace=True)
# count the number of NaN values in each column
print(dataset.isnull().sum())