import os, json
from datetime import datetime

def save_results(data, filename):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    os.makedirs("results", exist_ok=True)
    path = f"results/result_{timestamp}_{filename}.json"
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    return path
