import gzip
import pickle
import numpy as np

structured_dataset = {'label': [], 'valence': []}


def load_dataset(path):
    with gzip.open(path, "r") as dataset_file:
        dataset = pickle.load(dataset_file)

    return dataset

def prepare_data():
    dataset_raw = load_dataset('study_data_windowed/study_data_windowed_muse_30_s.gzip.pkl')

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
    structured_dataset['valence'].append(structured_dataset['label'][i]['sam']['VALENCE'])  # ok

    # print('Sample', i, signal_name, 'saved to structured file')

valence_list = structured_dataset['valence']

data = list(valence_list)
valence_list_array = np.array(data)

print(valence_list_array)
np.savetxt("valence_int.csv", valence_list_array, delimiter=",", fmt='%.i')

print('end')