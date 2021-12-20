from typing import List
from schema import FASTAEncodedRecord
from encode import encode_sequence
from exceptions import InvalidFileFormatException


def parse_fasta_dataset(
    file_path: str, encode_dataset: bool = True, max_seqs: int = -1
) -> List[FASTAEncodedRecord]:
    allowed_file_exts = ["fas", "fasta", "fna", "ffn", "faa", "frn", "fa"]
    if file_path.lower().split(".")[-1] not in allowed_file_exts:
        raise InvalidFileFormatException(
            "{} is invalid, must be one of: {}".format(file_path, allowed_file_exts)
        )

    dataset, current_idx, current_meta = [], 0, {}
    with open(file_path, "r") as f:
        for line in f.readlines(max_seqs):
            if line[0] == ">":
                if current_meta != {}:
                    current_meta["sequence"] = current_meta["sequence"].strip()
                    if encode_dataset:
                        current_meta["encoded_sequence"] = encode_sequence(
                            current_meta["sequence"]
                        )
                        record = FASTAEncodedRecord(**current_meta)
                    dataset.append(record)
                    current_meta = {}
                current_meta = {"id": line.replace("\n", "")}
                current_meta["sequence"] = ""
                current_idx += 1
            else:
                current_meta["sequence"] += line.replace("\n", " ")
    return dataset
