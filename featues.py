import pyeeg
import numpy as np
# from load_data import delta_TP9, prepare_data
from numpy.random import randn
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline, interpolate
from hurst import compute_Hc, random_walk

# delta=[]
# delta_TP9_new=int(delta_TP9 *10000000)
# numpy.savetxt('delta.txt', delta_TP9_int, delimiter='\n')
from load_timestamp import time
from pyeeg import bin_power, spectral_entropy

fid = open('delta_int3.txt', 'r')
tmp = fid.readlines()
data = [float(k) for k in tmp]

# frequencies
band = [0.5, 4, 7, 12, 30]
a = randn(4097)
# Evaluate Hurst equation


# def average_signal_val():
#     return sum(data) / len(data) in range(1, 100)


approximate = pyeeg.ap_entropy(data, 5, 1)
DFA = pyeeg.dfa(data)

# embed_seq = pyeeg.embed_seq(data, 1, 1)
first_order_diff = [data[i] - data[i - 1] for i in range(1, len(data))]
fisher_info = pyeeg.fisher_info(data, 1, 1, W=None)

# embed_seq = embed_seq(data)
hfd = pyeeg.hfd(data, 6)
hjorth = pyeeg.hjorth(data, D=None)

# Compute the Hurst exponent of X. If the output H=0.5,the behavior of the time-series is similar to random walk.
# #If H<0.5, the time-series cover less “distance” than a random walk, vice verse.
hurst = pyeeg.hurst(a)
PFD = pyeeg.pfd(data)
sam_ent = pyeeg.samp_entropy(data, 1, 2)
spectral_entropy = spectral_entropy(data, band, 256, Power_Ratio=None)
svd = pyeeg.svd_entropy(data, 6, 4, W=None)
PSI = pyeeg.bin_power(data, band, 256)

# print("average = ", average())
# numpy.savetxt('apen.txt', apen)


# Power Spectral Intensity (PSI) and Relative Intensity Ratio (RIR) Two 1- D v ec t o rs
print("bin_power = ", bin)
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
# print("embed_seq = ", embed_seq)
# Compute the first order difference of a time series.
# print("first_order_diff = ", first_order_diff)

# Plot
val = tmp

plt.plot(val)
plt.show()

print('end')
# print(len(DFA[22]['data']))
