import scipy
import numpy as np

def cross_correlation(sig1, sig2, mode='valid'):
    cc = scipy.signal.correlate(sig1-np.mean(sig1), sig2-np.mean(sig2), mode=mode) / (np.std(sig1) * np.std(sig2))
    cc /= min(len(sig1), len(sig2))
    return cc