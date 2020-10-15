import pandas as pd
import numpy as np

emotions_with_titles = pd.read_csv('../updated_9class.csv')


# new = pd.concat([features, emotions_with_titles], axis=1)


new = emotions_with_titles[(emotions_with_titles['Max'] >= 3)]
print(new)
# new.to_csv('nine.csv', index = False, header=False)

print('end')