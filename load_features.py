import gzip
import pickle


def load_dataset(path):
    with gzip.open(path, "r") as dataset_file:
        dataset = pickle.load(dataset_file)

    return dataset

whole_dataset = load_dataset('whole_dataset.p.gz')


print('end')
