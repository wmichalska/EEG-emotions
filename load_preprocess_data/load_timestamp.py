from helpers import load_dataset


def prepare_timestamp():
    dataset_timestamp = load_dataset('study_data_windowed/study_data_windowed_muse_30_s.gzip.pkl')

    # prepare data - remove inimportant aptributes
    for n in range(22, 65):
        for m in range(0, 11):
            del dataset_timestamp[n]['data'][m]['Delta_TP9']
            del dataset_timestamp[n]['data'][m]['Delta_AF7']
            del dataset_timestamp[n]['data'][m]['Delta_AF8']
            del dataset_timestamp[n]['data'][m]['Delta_TP10']
            del dataset_timestamp[n]['data'][m]['Theta_TP9']
            del dataset_timestamp[n]['data'][m]['Theta_AF7']
            del dataset_timestamp[n]['data'][m]['Theta_AF8']
            del dataset_timestamp[n]['data'][m]['Theta_TP10']
            del dataset_timestamp[n]['data'][m]['Alpha_TP9']
            del dataset_timestamp[n]['data'][m]['Alpha_AF7']
            del dataset_timestamp[n]['data'][m]['Alpha_AF8']
            del dataset_timestamp[n]['data'][m]['Alpha_TP10']
            del dataset_timestamp[n]['data'][m]['Beta_TP9']
            del dataset_timestamp[n]['data'][m]['Beta_AF7']
            del dataset_timestamp[n]['data'][m]['Beta_AF8']
            del dataset_timestamp[n]['data'][m]['Beta_TP10']
            del dataset_timestamp[n]['data'][m]['Gamma_TP9']
            del dataset_timestamp[n]['data'][m]['Gamma_AF7']
            del dataset_timestamp[n]['data'][m]['Gamma_AF8']
            del dataset_timestamp[n]['data'][m]['Gamma_TP10']
            del dataset_timestamp[n]['data'][m]['RAW_TP10']
            del dataset_timestamp[n]['data'][m]['RAW_AF7']
            del dataset_timestamp[n]['data'][m]['RAW_AF8']
            del dataset_timestamp[n]['data'][m]['RAW_TP9']
            del dataset_timestamp[n]['data'][m]['Accelerometer_X']
            del dataset_timestamp[n]['data'][m]['Accelerometer_Y']
            del dataset_timestamp[n]['data'][m]['Accelerometer_Z']
            del dataset_timestamp[n]['data'][m]['AUX_RIGHT']
            del dataset_timestamp[n]['data'][m]['Gyro_X']
            del dataset_timestamp[n]['data'][m]['Gyro_Y']
            del dataset_timestamp[n]['data'][m]['Gyro_Z']
            del dataset_timestamp[n]['data'][m]['HSI_TP9']
            del dataset_timestamp[n]['data'][m]['HSI_TP10']
            del dataset_timestamp[n]['data'][m]['HSI_AF7']
            del dataset_timestamp[n]['data'][m]['HSI_AF8']
            del dataset_timestamp[n]['data'][m]['HeadBandOn']
            del dataset_timestamp[n]['data'][m]['Battery']
    return dataset_timestamp

dataset_time = prepare_timestamp()

time = dataset_time[22]['data'][0]['time_stamp'].tolist()


print('nope')
