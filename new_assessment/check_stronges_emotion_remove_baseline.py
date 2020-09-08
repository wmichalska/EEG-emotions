import pandas as pd
import numpy as np

emotions_with_titles = pd.read_csv("przecinkami.csv")


# new = pd.concat([features, emotions_with_titles], axis=1)
# new = emotions_with_titles[emotions_with_titles['ids'].str.contains("")]
a = emotions_with_titles[~emotions_with_titles['Stimulant'].isin(['BASELINE'])]

# new = pd.concat([features, emotions_with_titles], axis=1)


new = a[(a['Max'] >= 3)]

# new.to_csv('nine.csv', index = False, header=False)

structured_emotions['Max'] = structured_emotions.idxmax(index=1)

# new = emotions_with_titles[(emotions_with_titles['Stimulant'] == 'BASELINE')]
# print(new)
# new.to_csv('nine_new.csv', index = False, header=False)

structure = {''}


print('end')