import json


def load_embeddings_from_json(file_path: str):
    with open(file_path) as f:
        return json.load(f)


def chunk_seq(seq: str, chunk_len: int = 10):
    ret_list = []
    chunk = ""
    for char in seq:
        chunk += char
        if len(chunk) % chunk_len == 0:
            ret_list.append(chunk)
            chunk = ""
    if chunk != "":
        ret_list.append("{}{}".format(chunk, "_" * (4 - len(chunk))))
    return ret_list
