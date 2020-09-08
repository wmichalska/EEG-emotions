import gzip
import pickle
import numpy as np
import pandas as pd

structured_dataset = {'label': [], 'AWE' :[], 'DISGUST':[], 'SURPRISE':[], 'ANGER':[], 'ENTHUSIASM':[], 'LIKING':[], 'FEAR':[], 'AMUSEMENT':[], 'SADNESS':[]}


def load_dataset(path):
    with gzip.open(path, "r") as dataset_file:
        dataset = pickle.load(dataset_file)

    return dataset

def prepare_data():
    dataset_raw = load_dataset('../study_data_windowed/study_data_windowed_muse_30_s.gzip.pkl')

    for n in range(22, 65):
            del dataset_raw[n]['data']
    del dataset_raw[27]
    del dataset_raw[58]


    return dataset_raw

dataset = prepare_data()

for participant_id, participant_all_data in dataset.items():
    for participant_data in participant_all_data['assessments']:
        structured_dataset['label'].append(participant_data)


sam_list = list(structured_dataset['label'][0]['sam'].keys())

for i in range(0, 451):
    structured_dataset['AWE'].append(structured_dataset['label'][i]['emotions']['AWE'])  # ok
    structured_dataset['DISGUST'].append(structured_dataset['label'][i]['emotions']['DISGUST'])  # ok
    structured_dataset['SURPRISE'].append(structured_dataset['label'][i]['emotions']['SURPRISE'])  # ok
    structured_dataset['ANGER'].append(structured_dataset['label'][i]['emotions']['ANGER'])  # ok
    structured_dataset['ENTHUSIASM'].append(structured_dataset['label'][i]['emotions']['ENTHUSIASM'])  # ok
    structured_dataset['LIKING'].append(structured_dataset['label'][i]['emotions']['LIKING'])  # ok
    structured_dataset['FEAR'].append(structured_dataset['label'][i]['emotions']['FEAR'])  # ok
    structured_dataset['AMUSEMENT'].append(structured_dataset['label'][i]['emotions']['AMUSEMENT'])  # ok
    structured_dataset['SADNESS'].append(structured_dataset['label'][i]['emotions']['SADNESS'])  # ok



    # print('Sample', i, signal_name, 'saved to structured file')

awe_list = structured_dataset['AWE']
disgust_list = structured_dataset['DISGUST']
surprise_list = structured_dataset['SURPRISE']
anger_list = structured_dataset['ANGER']
enthusiasm_list = structured_dataset['ENTHUSIASM']
liking_list = structured_dataset['LIKING']
fear_list = structured_dataset['FEAR']
amusement_list = structured_dataset['AMUSEMENT']
sadness_list = structured_dataset['SADNESS']




all_emotions = np.concatenate(([awe_list], [disgust_list], [surprise_list], [anger_list], [enthusiasm_list], [liking_list], [fear_list], [amusement_list], [sadness_list]))
structured_emotions = all_emotions.transpose()

# np.savetxt("valence_int.csv", valence_list_array, delimiter=",", fmt='%.i')
# np.savetxt("awe.csv", awe_list, delimiter=",", fmt='%.i')
# np.savetxt("all.csv", structured_emotions, delimiter=",", fmt='%.i')

# structured_emotions['Max'] = structured_emotions.idxmax()

print('end')