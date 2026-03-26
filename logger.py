import csv
from datetime import datetime

def log_request(prompt, model, reason, latency, cache_hit):
    with open("logs.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now(),
            prompt[:50],
            model,
            reason,
            latency,
            cache_hit
        ])