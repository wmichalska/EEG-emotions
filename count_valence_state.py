import pandas as pd

data = pd.read_csv("joined_features.csv")
valence = pd.read_csv("valence_int.csv")
valence_list = set(valence)

for i in valence_list:
    if i == 4:
        print ("Element negat")


print('done')