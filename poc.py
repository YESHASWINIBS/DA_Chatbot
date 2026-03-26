import json
from routing_model import route_prompt

with open("dataset.json") as f:
    data = json.load(f)

correct = 0
fp = 0
fn = 0

for item in data:
    pred, conf, _ = route_prompt(item["prompt"])
    actual = item["label"]

    print(f"{item['prompt']} → {pred} (Actual: {actual})")

    if pred == actual:
        correct += 1
    elif pred == "FAST" and actual == "CAPABLE":
        fn += 1
    elif pred == "CAPABLE" and actual == "FAST":
        fp += 1

accuracy = correct / len(data)

print("\n--- RESULTS ---")
print("Accuracy:", accuracy)
print("False Positives:", fp)
print("False Negatives:", fn)