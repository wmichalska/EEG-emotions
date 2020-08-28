import pyeeg
# import numpy
# from load_data import delta_TP9, prepare_data
from pyeeg import spectral_entropy, bin_power, hjorth
from numpy.random import randn

# delta=[]
# delta_TP9_new=int(delta_TP9 *10000000)
# numpy.savetxt('delta.txt', delta_TP9_int, delimiter='\n')

fid = open('delta_int.txt', 'r')
tmp = fid.readlines()
data = [float(k) for k in tmp]

# frequencies
band = [0.5, 4, 7, 12, 30]

ap_entropy = pyeeg.ap_entropy(data, 5, 1)
bin = bin_power(data, band, 256)
DFA = pyeeg.dfa(data)
embed_seq = pyeeg.embed_seq(data, 1, 1)
first_order_diff = [data[i] - data[i - 1] for i in range(1, len(data))]
fisher_info = pyeeg.fisher_info(data, 1, 1, W=None)
# embed_seq = embed_seq(data)
hfd = pyeeg.hfd(data, 6)
hjord = pyeeg.hjorth(data, D=None)
hurst = pyeeg.hurst(data)
PFD = pyeeg.pfd(data)
Ellipsis = pyeeg.pfd(data)
sam_ent = pyeeg.samp_entropy(data, 1,2 )
spectral_entropy = spectral_entropy(data, band, 256, Power_Ratio=None)
svd = pyeeg.svd_entropy(data, 6, 4, W=None)
PSI = pyeeg.bin_power(data, band, 256)

a = randn(4096)
A = pyeeg.hurst(a)


def average():
    return sum(first_order_diff) / len(first_order_diff) * 0000000.1


print("average = ", average())
# numpy.savetxt('apen.txt', apen)

print("ap_endropy = ", ap_entropy)
print("bin_power = ", bin)
print("DFA = ", DFA)
print("embed_seq", embed_seq)
print("first_order_diff = ", first_order_diff)
print("fisher_info", fisher_info)
print("Hurst_Exponent = ", A)
print("PFD = ", PFD)
print("Ellipsis = ", Ellipsis)
print("spectral_entropy = ", spectral_entropy)
print("approx entrophy = ", ap_entropy)

print('end')
# print(len(DFA[22]['data']))
