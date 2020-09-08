""" Script with helpful methods

"""
import gzip
import os
import pickle

import pandas as pd

signal_frequency = {
    'BVP': 64,
    'GSR': 4,
    # 'EDA': 4,
    'TEMP': 4,
    # 'ACC': 32,
    'ACC_X': 32,
    'ACC_Y': 32,
    'ACC_Z': 32,
}


def get_muse_sampling():
    return 256


datetime_format_questionnaire = '%a, %d %b %Y %H:%M:%S %Z'
datetime_format_assessment = '%Y-%m-%dT%H:%M:%S'

muse_dtypes = {
    'time_stamp': 'datetime64[ms]', 'Delta_TP9': float, 'Delta_AF7': float,
    'Delta_AF8': float, 'Delta_TP10': float, 'Theta_TP9': float,
    'Theta_AF7': float, 'Theta_AF8': float, 'Theta_TP10': float,
    'Alpha_TP9': float, 'Alpha_AF7': float, 'Alpha_AF8': float, 'Alpha_TP10': float,
    'Beta_TP9': float, 'Beta_AF7': float, 'Beta_AF8': float, 'Beta_TP10': float,
    'Gamma_TP9': float, 'Gamma_AF7': float, 'Gamma_AF8': float, 'Gamma_TP10': float,
    'RAW_TP9': float, 'RAW_AF7': float, 'RAW_AF8': float, 'RAW_TP10': float,
    'AUX_RIGHT': float, 'Accelerometer_X': float, 'Accelerometer_Y': float,
    'Accelerometer_Z': float, 'Gyro_X': float, 'Gyro_Y': float, 'Gyro_Z': float,
    'HeadBandOn': float, 'HSI_TP9': float, 'HSI_AF7': float, 'HSI_AF8': float,
    'HSI_TP10': float, 'Battery': float, 'Elements': 'string',
}

video_types = ['NEUT', 'DISGUST', 'ANGER', 'AMUSEMENT', 'SURPRISE', 'AWE',
               'ENTHUSIASM', 'LIKING', 'BASELINE', 'SADNESS', 'FEAR']

# not all participant answered proper about their age
# this data is from theirs registration forms
participant_age_gender = [('21', 'k'), ('23', 'm'), ('29', 'm'), ('24', 'm'), ('19', 'k'), ('25', 'k'), ('23', 'm'),
                          ('24', 'm'), ('21', 'm'), ('24', 'm'), ('25', 'k'), ('21', 'm'), ('26', 'k'), ('24', 'm'),
                          ('29', 'k'), ('23', 'k'), ('22', 'm'), ('21', 'k'), ('26', 'k'), ('23', 'k'), ('26', 'k'),
                          ('25', 'k'), ('21', 'k'), ('24', 'k'), ('22', 'k'), ('23', 'm'), ('23', 'm'), ('21', 'm'),
                          ('29', 'm'), ('23', 'm'), ('21', 'm'), ('21', 'k'), ('22', 'k'), ('23', 'm'), ('22', 'm'),
                          ('22', 'k'), ('23', 'k'), ('23', 'm'), ('21', 'k'), ('25', 'k'), ('24', 'm'), ('23', 'm'),
                          ('25', 'k')]


def save_dataset(path, dataset_name, dataset):
    os.makedirs(path, exist_ok=True)
    with gzip.open(f"{path}/{dataset_name}.gzip.pkl", "wb") as dataset_file:
        # protocol = -1
        pickle.dump(dataset, dataset_file, )


def load_dataset(path):
    if path[-9:] != '.gzip.pkl':
        path += '.gzip.pkl'

    with gzip.open(path, "r") as dataset_file:
        dataset = pickle.load(dataset_file)

    return dataset


def get_participant_seen_films():
    participant_seen_films = pd.read_csv('seen_videos.tsv',
                                         sep='\t', index_col=0)
    del participant_seen_films['Unnamed: 11']
    return participant_seen_films.to_dict(orient='index')
