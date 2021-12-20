import json


def load_embeddings_from_json(file_path: str):
    with open(file_path) as f:
        return json.load(f)