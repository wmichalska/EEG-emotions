import gzip
import os
import pickle

import pandas as pd

structured_dataset = {'data': [], 'label': [], 'features': []}

def load_dataset(path):
    if path[-9:] != '.gzip.pkl':
        path += '.gzip.pkl'

    with gzip.open(path, "r") as dataset_file:
        dataset = pickle.load(dataset_file)

    return dataset

dataset_raw = load_dataset('study_data_windowed_muse_30_s.gzip.pkl')

print('end')