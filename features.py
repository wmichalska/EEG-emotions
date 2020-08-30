import pyeeg
import numpy as np
from numpy.random import randn

from load_data import participant_data, structured_dataset, signals_list
from pyeeg import bin_power, spectral_entropy
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline, interpolate
from hurst import compute_Hc, random_walk
from pyeeg import bin_power, spectral_entropy

# delta=[]
# delta_TP9_new=int(delta_TP9 *10000000)
# numpy.savetxt('delta.txt', delta_TP9_int, delimiter='\n')

# zizz = open('Z001.txt', 'r')
# zzz = zizz.readlines()
# zewww = [float(k) for k in zzz]
#
# fid = open('delta_int3.txt', 'r')
# tmp = fid.readlines()
# k: int
# data = [float(k) for k in tmp]
# data_int = tmp.astype(int)

data_list = [['data'], ['data0'], ['data1'], ['data2'], ['data3']]

data = structured_dataset['data'][0]['Delta_TP9']
data0 = structured_dataset['data'][0]['Delta_TP9']
data1 = structured_dataset['data'][0]['Delta_TP10']
data2 = structured_dataset['data'][0]['Delta_AF7']
data3 = structured_dataset['data'][0]['Delta_AF8']

# for participant_data in data_list:
# all_signals = {[data0], [data1], [data2], [data3]}

# for item in all_signals:
# frequencies


# def get_features():
band = [0.5, 4, 7, 12, 30]
a = randn(4097)
approximate = pyeeg.ap_entropy(data, 5, 1)
DFA = pyeeg.dfa(data)
first_order_diff = [data[i] - data[i - 1] for i in range(1, len(data))]
fisher_info = pyeeg.fisher_info(data, 1, 1, W=None)
embed_seq = pyeeg.embed_seq(data, 1, 1)
hfd = pyeeg.hfd(data, 6)
hjorth = pyeeg.hjorth(data, D=None)
hurst = pyeeg.hurst(data)
PFD = pyeeg.pfd(data)
sam_ent = pyeeg.samp_entropy(data, 1, 2)
spectral_entropy = spectral_entropy(data, band, 256, Power_Ratio=None)
svd = pyeeg.svd_entropy(data, 6, 4, W=None)
PSI = pyeeg.bin_power(data, band, 256)
    # return [approximate, DFA, fisher_info, embed_seq, hfd,hjorth,hurst, PFD, sam_ent, spectral_entropy, svd, PSI]

# for n in structured_dataset['data'][n]['Delta_TP9']:

# Power Spectral Intensity (PSI) and Relative Intensity Ratio (RIR) Two 1- D v ec t o rs
print("bin_power = ", PSI)
# Petrosian Fractal Dimension (PFD) Ascalar
print("PFD = ", PFD)
# Higuchi Fractal Dimension (HFD) Ascalar
print("hfd = ", hfd)
# Hjorth mobility and complexity Two s c a la rs
print("hjorth = ", hjorth)
# Spectral Entropy (Shannon’s entropy of RIRs) Ascalar
print("spectral_entropy = ", spectral_entropy)
# SVD Entropy Ascalar
print("svd = ", svd)
# Fisher Information Ascalar
print("fisher_info = ", fisher_info)
# Approximate Entropy (ApEn) Ascalar
print("approx entrophy = ", approximate)
# Detrended Fluctuation Analysis (DFA) Ascalar
print("DFA = ", DFA)
# HurstExponent(Hurst) Ascalar
print("Hurst_Exponent = ", hurst)
# Build a set of embedding sequences from given time series X with lag Tau and embedding dimension
print("embed_seq = ", embed_seq)
# Compute the first order difference of a time series.
print("first_order_diff = ", first_order_diff)

print('end')
