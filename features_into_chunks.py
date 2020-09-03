import numpy as np
from load_features import DFA_chunks, list_of_DFA, list_of_hfd, list_of_sam_ent, list_of_PFD, list_of_spectral_entropy, \
    list_of_svd

DFA_chunks = [list_of_DFA[x:x + 473] for x in range(0, len(list_of_DFA), 473)]
hfd_chunks = [list_of_hfd[x:x + 473] for x in range(0, len(list_of_hfd), 473)]
PFD_chunks = [list_of_PFD[x:x + 473] for x in range(0, len(list_of_PFD), 473)]
sam_ent_chunks = [list_of_sam_ent[x:x + 473] for x in range(0, len(list_of_sam_ent), 473)]
spectral_entropy_chunks = [list_of_spectral_entropy[x:x + 473] for x in range(0, len(list_of_spectral_entropy), 473)]
svd_chunks = [list_of_svd[x:x + 473] for x in range(0, len(list_of_svd), 473)]

DFA_array = np.array(DFA_chunks)
hfd_array = np.array(hfd_chunks)
PFD_array = np.array(PFD_chunks)
sam_ent_array = np.array(sam_ent_chunks)
spectral_entropy_array = np.array(spectral_entropy_chunks)
svd_array = np.array(svd_chunks)


joined_features = np.concatenate((DFA_array, hfd_array, PFD_array, sam_ent_array, spectral_entropy_array, svd_array))

structured_features = joined_features.transpose()
a = np.asarray(structured_features)
np.savetxt("structured_features.csv", a, delimiter=",")



print('end')