
import pandas as pd
from datetime import datetime

def log_inference(input_data, prediction, log_path="data/logs.csv"):
    log_entry = {
        **input_data,
        "prediction": prediction,
        "timestamp": datetime.utcnow().isoformat(),
        "model_version": "v1.0"
    }
    pd.DataFrame([log_entry]).to_csv(log_path, mode='a', header=False)

if __name__ == "__main__":
    sample_input = {"feature1": 1.3, "feature2": 105}
    log_inference(sample_input, prediction=1)
