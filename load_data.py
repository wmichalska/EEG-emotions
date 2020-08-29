import numpy
from numpy.matlib import randn
from pandas import date_range, Series
import math
from helpers import load_dataset
import matplotlib.pyplot as plt
import pandas as pd

frequency = ["Alpha", "Beta", "Gamma", "Delta", "Theta"]
electrode = ["AF7", "AF8", "TP9", "TP10"]


# print(frequency,  electrode)

def prepare_data():
    dataset_raw = load_dataset('study_data_windowed/study_data_windowed_muse_30_s.gzip.pkl')

    for n in range(22, 65):
        for m in range(0, 11):
            del dataset_raw[n]['data'][m]['time_stamp']
            del dataset_raw[n]['data'][m]['Accelerometer_X']
            del dataset_raw[n]['data'][m]['Accelerometer_Y']
            del dataset_raw[n]['data'][m]['Accelerometer_Z']
            del dataset_raw[n]['data'][m]['AUX_RIGHT']
            del dataset_raw[n]['data'][m]['Gyro_X']
            del dataset_raw[n]['data'][m]['Gyro_Y']
            del dataset_raw[n]['data'][m]['Gyro_Z']
            del dataset_raw[n]['data'][m]['RAW_TP9']
            del dataset_raw[n]['data'][m]['RAW_TP10']
            del dataset_raw[n]['data'][m]['RAW_AF7']
            del dataset_raw[n]['data'][m]['RAW_AF8']
            del dataset_raw[n]['data'][m]['HSI_TP9']
            del dataset_raw[n]['data'][m]['HSI_TP10']
            del dataset_raw[n]['data'][m]['HSI_AF7']
            del dataset_raw[n]['data'][m]['HSI_AF8']
            del dataset_raw[n]['data'][m]['HeadBandOn']
            del dataset_raw[n]['data'][m]['Battery']
    return dataset_raw


dataset = prepare_data()

# get all signal lst names
signals_list = list(dataset[22]['data'][0].keys())

structured_dataset = {'data': [], 'label': []}

# divide all electrodes and bands for all participants
for participant_id, participant_all_data in dataset.items():
    for participant_data in participant_all_data['data']:
        # interpolation is done in below loop
        for signal_name in signals_list:
            participant_data[signal_name] = pd.Series(participant_data[signal_name]).interpolate(method='polynomial', order=2).to_numpy().tolist()
        structured_dataset['data'].append(participant_data)
        # for signal_name, signal_data in participant_data.items():

        # for signal in signals_list:
        #     participant_data[signal]
        # delta_TP9 = participant_data['Delta_TP9']

# # interpolate existing data
# for data in structured_dataset.data:
#     data
#

# delta_TP9 = dataset[22]['data'][0]['Delta_TP9'].tolist()
# for k in range(0, 474):
#     signals_list_raw_delta_tp9 = structured_dataset['data'][k]['Delta_TP9']
#     signals_list_raw_delta_tp10 = structured_dataset['data'][k]['Delta_TP10']
#     signals_list_raw_delta_af7 = structured_dataset['data'][k]['Delta_AF7']
#

# signals_list_raw = [[]]

# for signal_name in signals_list:
#     single_signal = []
#     for t in range(0, 472):
#         single_signal.append(structured_dataset['data'][t][signal_name].tolist())
#     signals_list_raw.append(single_signal)

# df = pd.DataFrame({'tp9': signals_list_raw[1][0]}).interpolate().values.tolist()
# signals_list_raw[1][0] =

print("done")
# numpy.savetxt('delta_int4.txt', new_list, delimiter='\n', fmt='%i')

# delta_int = delta_TP9 * 100000000

# numpy.savetxt('delta_int.txt', delta_int, delimiter='\n', fmt='%.7f')


# Hurst_Exponent = pyeeg.hurst(dataset)
# PFD = pyeeg.pfd(dataset)
# Ellipsis = pyeeg.pfd(dataset[22])

# print(delta_TP9)
