import numpy as np

def compare_signals(signal1, signal2, threshold):
    signal1 = (signal1 - np.mean(signal1)) / np.std(signal1)
    signal2 = (signal2 - np.mean(signal2)) / np.std(signal2)
    correlation = np.correlate(signal1, signal2, mode='full')
    max_correlation = np.max(correlation) / (len(signal1) * np.std(signal1) * np.std(signal2))
    return max_correlation > threshold