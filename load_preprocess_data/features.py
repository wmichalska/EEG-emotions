import pyeeg
from numpy.random import randn

def calculate_features(samples):
    data = samples
    if not samples:
        print("no samples")
        return []

    band = [0.5, 4, 7, 12, 30]
    a = randn(4097)
    # approx = pyeeg.ap_entropy(data, 5, 1)
    approx = 0
    DFA = pyeeg.dfa(data)
    first_order_diff = [data[i] - data[i - 1] for i in range(1, len(data))]
    fisher_info = pyeeg.fisher_info(data, 1, 1, W=None)
    embed_seq = pyeeg.embed_seq(data, 1, 1)
    hfd = pyeeg.hfd(data, 6)
    hjorth = pyeeg.hjorth(data, D=None)
    hurst = pyeeg.hurst(data)
    PFD = pyeeg.pfd(data)
    sam_ent = pyeeg.samp_entropy(data, 1, 2)
    spectral_entropy = pyeeg.spectral_entropy(data, band, 256, Power_Ratio=None)
    svd = pyeeg.svd_entropy(data, 6, 4, W=None)
    PSI = pyeeg.bin_power(data, band, 256)

    # # Power Spectral Intensity (PSI) and Relative Intensity Ratio (RIR) Two 1- D v ec t o rs
    # # print("bin_power = ", PSI)
    # # Petrosian Fractal Dimension (PFD) Ascalar
    # print("PFD = ", PFD)
    # # Higuchi Fractal Dimension (HFD) Ascalar
    # print("hfd = ", hfd)
    # # Hjorth mobility and complexity Two s c a la rs
    # print("hjorth = ", hjorth)
    # # Spectral Entropy (Shannon’s entropy of RIRs) Ascalar
    # print("spectral_entropy = ", spectral_entropy)
    # # SVD Entropy Ascalar
    # print("svd = ", svd)
    # # Fisher Information Ascalar
    # print("fisher_info = ", fisher_info)
    # # Approximate Entropy (ApEn) Ascalar
    # print("approx entrophy = ", approx)
    # # Detrended Fluctuation Analysis (DFA) Ascalar
    # print("DFA = ", DFA)
    # # HurstExponent(Hurst) Ascalar
    # print("Hurst_Exponent = ", hurst)
    # # Build a set of embedding sequences from given time series X with lag Tau and embedding dimension
    # print("embed_seq = ", embed_seq)
    # # Compute the first order difference of a time series.
    # print("first_order_diff = ", first_order_diff)

    return {'approximate': approx, 'DFA': DFA, 'fisher_info': fisher_info, 'embed_seq': embed_seq, 'hfd': hfd,
            'hjorth': hjorth,
            'hurst': hurst, 'PFD': PFD, 'sam_ent': sam_ent, 'spectral_entropy': spectral_entropy, 'svd': svd,
            'PSI': PSI,
            'first_order_diff': first_order_diff}
