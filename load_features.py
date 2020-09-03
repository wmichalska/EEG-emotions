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

structured_features = {'DFA': [], 'hfd': [],
                       'hjorth': [],
                       'PFD': [], 'sam_ent': [], 'spectral_entropy': [], 'svd': [],
                       'PSI': []}

# signal_features = {'id': [], 'signal_name': [], 'feature_name': [], 'feature_value': []}
print('1')

for i in range(0, 473):
    for signal_name in signals_list:
        structured_features['DFA'].append(extract_signal_feature_value(whole_dataset, i, signal_name, 'DFA'))  # ok
        # structured_features['fisher_info'].append(
        #     extract_signal_feature_value(whole_dataset, i, signal_name, 'fisher_info')) # zeros
        # structured_features['embed_seq'].append(
        #     extract_signal_feature_value(whole_dataset, i, signal_name, 'embed_seq')) # PREPROCESS sequence od 6600 elements
        structured_features['hfd'].append(
            extract_signal_feature_value(whole_dataset, i, signal_name, 'hfd'))  # some elements < 0
        structured_features['hjorth'].append(
            extract_signal_feature_value(whole_dataset, i, signal_name, 'hjorth'))  # tuple of 2 elements
        # structured_features['hurst'].append(extract_signal_feature_value(whole_dataset, i, signal_name, 'hurst')) #nan
        structured_features['PFD'].append(
            extract_signal_feature_value(whole_dataset, i, signal_name, 'PFD'))  # some elemets  = 1
        structured_features['sam_ent'].append(
            extract_signal_feature_value(whole_dataset, i, signal_name, 'sam_ent'))  # most elements 0.00003xx
        structured_features['spectral_entropy'].append(
            extract_signal_feature_value(whole_dataset, i, signal_name, 'spectral_entropy'))  # ok, most =0.5 +- 0.1
        structured_features['svd'].append(
            extract_signal_feature_value(whole_dataset, i, signal_name, 'svd'))  # ok, most elements 0.2-0.5
        structured_features['PSI'].append(extract_signal_feature_value(whole_dataset, i, signal_name,
                                                                       'PSI'))  # every element is a tuple of 2 arrays of 4 values
        # structured_features['first_order_diff'].append(
        # extract_signal_feature_value(whole_dataset, i, signal_name, 'first_order_diff')) # PREPROCESS every 16 element diff than 0
    # print('Sample', i, signal_name, 'saved to structured file')

# filename = "structured_features.p.gz"
# with gzip.open(filename, 'wb') as f:
#     pickle.dump(structured_features, f)
#     print('ALL Samples saved to structured file')


list_of_DFA = structured_features['DFA']
list_of_hfd = structured_features['hfd']
list_of_hjorth = structured_features['hjorth']  # 2 elements
list_of_PFD = structured_features['PFD']
list_of_sam_ent = structured_features['sam_ent']
list_of_spectral_entropy = structured_features['spectral_entropy']
list_of_svd = structured_features['svd']
list_of_PSI = structured_features['PSI']  # tuple of 2 lists with 4 elements

DFA_chunks = [list_of_DFA[x:x + 473] for x in range(0, len(list_of_DFA), 473)]
hfd_chunks = [list_of_hfd[x:x + 473] for x in range(0, len(list_of_hfd), 473)]
PFD_chunks = [list_of_PFD[x:x + 473] for x in range(0, len(list_of_PFD), 473)]
sam_ent_chunks = [list_of_sam_ent[x:x + 473] for x in range(0, len(list_of_sam_ent), 473)]
spectral_entropy_chunks = [list_of_spectral_entropy[x:x + 473] for x in range(0, len(list_of_spectral_entropy), 473)]
svd_chunks = [list_of_svd[x:x + 473] for x in range(0, len(list_of_svd), 473)]

variances = {'DFA':[], 'hfd': [], }

for i in range(0, 20):
    DFA_variance = np.nanvar(DFA_chunks[i])
    print(DFA_variance)
    variances['DFA'].append(DFA_variance)



print('end')
