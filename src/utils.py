import json

def load_data(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(obj, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(obj, f, indent=4, ensure_ascii=False)
