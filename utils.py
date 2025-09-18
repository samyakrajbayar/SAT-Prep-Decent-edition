import json
import os

def load_json(path):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def merge_dataset(existing, new):
    ids = {q["id"] for q in existing}
    added = 0
    for item in new:
        if item["id"] not in ids:
            existing.append(item)
            ids.add(item["id"])
            added += 1
    return existing, added
