
import pandas as pd
from scipy.stats import ks_2samp

def detect_drift(current_data, reference_data, threshold=0.05):
    report = {}
    for col in reference_data.columns:
        stat, p = ks_2samp(reference_data[col], current_data[col])
        report[col] = {"p_value": p, "drift_detected": p < threshold}
    return report

if __name__ == "__main__":
    ref = pd.read_csv("data/reference_data.csv")
    cur = pd.read_csv("data/current_data.csv")
    report = detect_drift(cur, ref)
    print("Drift Report:", report)
