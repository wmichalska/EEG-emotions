import numpy as np
import pandas as pd

features = pd.read_csv("structured_features_deleted.csv")
valence = pd.read_csv('../valence_int.csv')

transpose_features = features.transpose()
transpose_valence = valence.transpose()
# joined_features_valence = np.concatenate((transpose_features, valence))

result = pd.concat([features, valence], axis=1)
print(result.shape)
a = np.asarray(result)
np.savetxt("joined_features_int.csv", a, delimiter=",")


print('end')
