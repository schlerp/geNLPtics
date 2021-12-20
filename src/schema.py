from typing import List
import pydantic


NucleotideEmbedding = List[float]


class FASTAEncodedRecord(pydantic.BaseModel):
    id: str
    sequence: str
    encoded_sequence: List[NucleotideEmbedding]
