import numpy
from numpy.matlib import randn
from pandas import date_range, Series

from helpers import load_dataset
import matplotlib.pyplot as plt

# dataset = load_dataset('study_data_windowed/study_data_windowed_muse_30_s.gzip.pkl')

frequency = ["Alpha", "Beta", "Gamma", "Delta", "Theta"]
electrode = ["AF7", "AF8", "TP9", "TP10"]


# print(frequency,  electrode)

def prepare_data():
    dataset_raw = load_dataset('study_data_windowed/study_data_windowed_muse_30_s.gzip.pkl')

    # prepare data - remove inimportant aptributes
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

# divide all elestrodes and bands for all participants
for participant_id, participant_all_data in dataset.items():
    for participant_data in participant_all_data['data']:
        structured_dataset['data'].append(participant_data)
        # for signal_name, signal_data in participant_data.items():

        # for signal in signals_list:
        #     participant_data[signal]
        # delta_TP9 = participant_data['Delta_TP9']

all_delta_1_1 = structured_dataset['data'][0]['Delta_TP9'].tolist()
all_delta_1_2 = structured_dataset['data'][1]['Delta_TP9'].tolist()
all_delta_1_3 = structured_dataset['data'][2]['Delta_TP9'].tolist()
all_delta_1_4 = structured_dataset['data'][3]['Delta_TP9'].tolist()
all_delta_1_5 = structured_dataset['data'][4]['Delta_TP9'].tolist()
print("Lengh of all delta for 1st person for 1st movie = ", len(all_delta_1_1))
print("Lengh of all delta for 1st person for 2st movie = ", len(all_delta_1_2))
print("Lengh of all delta for 1st person for 3st movie = ", len(all_delta_1_3))
print("Lengh of all delta for 1st person for 4st movie = ", len(all_delta_1_4))
print("Lengh of all delta for 1st person for 5st movie = ", len(all_delta_1_5))

# delta_TP9 = dataset[22]['data'][0]['Delta_TP9'].tolist()

# multiplied_list = [element * 100000000 for element in delta_TP9]
# numpy.savetxt('delta_int3.txt', multiplied_list, delimiter='\n', fmt='%i')

# delta_int = delta_TP9 * 100000000

# numpy.savetxt('delta_int.txt', delta_int, delimiter='\n', fmt='%.7f')


plt.plot(all_delta_1_1, label='1st')
plt.plot(all_delta_1_2, label='2st')
plt.plot(all_delta_1_3, label='3st')
plt.plot(all_delta_1_4, label='4st')
plt.plot(all_delta_1_5, label='5st')

plt.grid()
plt.xlabel('sample [number]')
plt.ylabel('brainwaves [Bels]')
plt.title('Delta_TP9 participant 22')
plt.legend()
plt.show()

# Hurst_Exponent = pyeeg.hurst(dataset)
# PFD = pyeeg.pfd(dataset)
# Ellipsis = pyeeg.pfd(dataset[22])

# print(delta_TP9)
print('nope')
