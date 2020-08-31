import gzip
import pickle
import numpy as np


def load_dataset(path):
    with gzip.open(path, "r") as dataset_file:
        dataset = pickle.load(dataset_file)

    return dataset


def get_signal_name(signal_id):
    if signal_id == 0:
        return 'Delta_TP9'
    if signal_id == 1:
        return 'Delta_AF7'
    if signal_id == 2:
        return 'Delta_AF8'
    if signal_id == 3:
        return 'Delta_TP10'

    if signal_id == 4:
        return 'Theta_TP9'
    if signal_id == 5:
        return 'Theta_AF7'
    if signal_id == 6:
        return 'Theta_AF8'
    if signal_id == 7:
        return 'Theta_TP10'

    if signal_id == 8:
        return 'Alpha_TP9'
    if signal_id == 9:
        return 'Alpha_AF7'
    if signal_id == 10:
        return 'Alpha_AF8'
    if signal_id == 11:
        return 'Alpha_TP10'

    if signal_id == 12:
        return 'Beta_TP9'
    if signal_id == 13:
        return 'Beta_AF7'
    if signal_id == 14:
        return 'Beta_AF8'
    if signal_id == 15:
        return 'Beta_TP10'

    if signal_id == 16:
        return 'Gamma_TP9'
    if signal_id == 17:
        return 'Gamma_AF7'
    if signal_id == 18:
        return 'Gamma_AF8'
    if signal_id == 19:
        return 'Gamma_TP10'


def get_signal_id(signal_name):
    if signal_name == 'Delta_TP9':
        return 0
    if signal_name == 'Delta_AF7':
        return 1
    if signal_name == 'Delta_AF8':
        return 2
    if signal_name == 'Delta_TP10':
        return 3

    if signal_name == 'Theta_TP9':
        return 4
    if signal_name == 'Theta_AF7':
        return 5
    if signal_name == 'Theta_AF8':
        return 6
    if signal_name == 'Theta_TP10':
        return 7

    if signal_name == 'Alpha_TP9':
        return 8
    if signal_name == 'Alpha_AF7':
        return 9
    if signal_name == 'Alpha_AF8':
        return 10
    if signal_name == 'Alpha_TP10':
        return 11

    if signal_name == 'Beta_TP9':
        return 12
    if signal_name == 'Beta_AF7':
        return 13
    if signal_name == 'Beta_AF8':
        return 14
    if signal_name == 'Beta_TP10':
        return 15

    if signal_name == 'Gamma_TP9':
        return 16
    if signal_name == 'Gamma_AF7':
        return 17
    if signal_name == 'Gamma_AF8':
        return 18
    if signal_name == 'Gamma_TP10':
        return 19


def extract_signal_feature_value(dataset, dataset_id, signal_name, feature_name):
    signal_id = get_signal_id(signal_name)
    signal_dict = dataset['features'][dataset_id][signal_id][signal_name]
    if isinstance(signal_dict, dict):
        return signal_dict[feature_name]

    return 0


whole_dataset = load_dataset('whole_dataset.p.gz')
signals_list = list(whole_dataset['data'][0].keys())

structured_features = {'approximate': [], 'DFA': [], 'fisher_info': [], 'embed_seq': [], 'hfd': [],
                       'hjorth': [],
                       'hurst': [], 'PFD': [], 'sam_ent': [], 'spectral_entropy': [], 'svd': [],
                       'PSI': [],
                       'first_order_diff': []}

# signal_features = {'id': [], 'signal_name': [], 'feature_name': [], 'feature_value': []}
print('1')

valid_dataset_ids = [0, 11, 22, 33]

for i in range(0, 473):
    for signal_name in signals_list:
        structured_features['DFA'].append(extract_signal_feature_value(whole_dataset, i, signal_name, 'DFA'))
        structured_features['fisher_info'].append(
            extract_signal_feature_value(whole_dataset, i, signal_name, 'fisher_info'))
        structured_features['embed_seq'].append(
            extract_signal_feature_value(whole_dataset, i, signal_name, 'embed_seq'))
        structured_features['hfd'].append(extract_signal_feature_value(whole_dataset, i, signal_name, 'hfd'))
        structured_features['hjorth'].append(extract_signal_feature_value(whole_dataset, i, signal_name, 'hjorth'))
        structured_features['hurst'].append(extract_signal_feature_value(whole_dataset, i, signal_name, 'hurst'))
        structured_features['PFD'].append(extract_signal_feature_value(whole_dataset, i, signal_name, 'PFD'))
        structured_features['sam_ent'].append(extract_signal_feature_value(whole_dataset, i, signal_name, 'sam_ent'))
        structured_features['spectral_entropy'].append(
            extract_signal_feature_value(whole_dataset, i, signal_name, 'spectral_entropy'))
        structured_features['svd'].append(extract_signal_feature_value(whole_dataset, i, signal_name, 'svd'))
        structured_features['PSI'].append(extract_signal_feature_value(whole_dataset, i, signal_name, 'PSI'))
        structured_features['first_order_diff'].append(
            extract_signal_feature_value(whole_dataset, i, signal_name, 'first_order_diff'))
    print('Sample', i, signal_name, 'saved to structured file')

filename = "structured_features.p.gz"
with gzip.open(filename, 'wb') as f:
    pickle.dump(structured_features, f)
    print('ALL Samples saved to structured file')

list_of_DFA = structured_features['DFA']
list_of_fisher_info = structured_features['fisher_info']

DFA_variance = np.nanvar(list_of_DFA)
fisher_info_variance = np.nanvar(list_of_fisher_info)
print(DFA_variance, fisher_info_variance)

print('end')
