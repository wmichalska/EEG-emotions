from multiprocessing import Process, Manager
from features import calculate_features
from helpers import load_dataset
import pandas as pd
from datetime import datetime
import gzip
import pickle

structured_dataset = {'data': [], 'label': [], 'features': []}

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


def worker_job(data, list_to_append, signals_list):
    for signal_name in signals_list:
        list_to_append.append({signal_name: calculate_features(data[signal_name])})
        print("calculated ", signal_name, datetime.now().time())


def main():
    frequency = ["Alpha", "Beta", "Gamma", "Delta", "Theta"]
    electrode = ["AF7", "AF8", "TP9", "TP10"]

    manager = Manager()

    dataset = prepare_data()

    # get all signal list names
    signals_list = list(dataset[22]['data'][0].keys())
    all_emotions = list(dataset[22]['assessments'][0]['emotions'].keys())
    assessment_types = list(dataset[22]['assessments'][0].keys())
    sam_list = list(dataset[22]['assessments'][0]['sam'].keys())

    # divide all electrodes and bands for all participants
    for participant_id, participant_all_data in dataset.items():
        for participant_data in participant_all_data['data']:
            # interpolation is done in below loop
            for signal_name in signals_list:
                participant_data[signal_name] = pd.Series(participant_data[signal_name]).interpolate(
                    method='polynomial',
                    order=2).to_numpy().tolist()
            structured_dataset['data'].append(participant_data)

    for participant_id, participant_all_data in dataset.items():
        for participant_data in participant_all_data['assessments']:
            structured_dataset['label'].append(participant_data)

    # jobs = []
    # # calculate features
    # for i, data in enumerate(structured_dataset['data']):
    #     structured_dataset['features'].append(manager.list())
    #     p = Process(target=worker_job, args=(data, structured_dataset['features'][i], signals_list))
    #     print("created thread")
    #     jobs.append(p)
    #     p.start()
    #     # structured_dataset['features'][i].append({signal_name: calculate_features(data[signal_name])})
    #
    # for job in jobs:
    #     print("joining thread!")
    #     job.join()
    ######################################################################

    # calculate features
    # for i, data in enumerate(structured_dataset['data']):
    #     structured_dataset['features'].append([])
    #     for signal_name in signals_list:
    #         structured_dataset['features'][i].append({signal_name: calculate_features(data[signal_name])})
    #         print("calculated ", signal_name, datetime.now().time())
    #     print("done i=", i)
    #
    #     filename = "features" + str(i) + ".p.gz"
    #     with gzip.open(filename, 'wb') as f:
    #         pickle.dump(structured_dataset['features'][i], f)
    #         print("saved file i=", i)
    #
    # filename = "whole_dataset.p.gz"
    # with gzip.open(filename, 'wb') as f:
    #     pickle.dump(structured_dataset, f)

    # calculate_features(structured_dataset['data'][80]['Delta_TP9'])

    print("done")


if __name__ == "__main__":
    main()
