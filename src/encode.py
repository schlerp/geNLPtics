from typing import List
from utils import load_embeddings_from_json


base_embedding_dict = load_embeddings_from_json("./nucleotide_embedding.json")


def encode_sequence(sequence: str) -> List[List[float]]:
    return [
        base_embedding_dict.get(z, base_embedding_dict["-"])
        for z in sequence.strip().replace(" ", "")
    ]
