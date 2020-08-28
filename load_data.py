from helpers import load_dataset

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

# delta_TP9 = dataset[22]['data'][0]['Delta_TP9'].tolist()

# data_TP9_int = [int(i * 10000000) for i in delta_TP9]
# numpy.savetxt('delta_int.txt', data_TP9_int, delimiter='\n', fmt='%f')

# delta_int = delta_TP9 * 100000000

# numpy.savetxt('delta_int.txt', delta_int, delimiter='\n', fmt='%.7f')


# Hurst_Exponent = pyeeg.hurst(dataset)
# PFD = pyeeg.pfd(dataset)
# Ellipsis = pyeeg.pfd(dataset[22])

# print(delta_TP9)
print('nope')
