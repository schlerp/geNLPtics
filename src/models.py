from typing import Tuple, List
from schema import FASTAEncodedRecord


class BaseModel(object):
    def __init__(self, input_shape: Tuple, output_shape: Tuple):
        self.input_shape = input_shape
        self.output_shape = output_shape
        self.embeddings = None

    def get_embeddings(self):
        return self.embeddings

    def fit(
        self,
        dataset: List[FASTAEncodedRecord],
        epochs: int = 10,
    ):
        pass


class ConvolutionalModel(BaseModel):
    def __init__(self, input_shape: Tuple, output_shape: Tuple, width: int = 32):
        super().__init__(input_shape, output_shape)
        self.width = width

    def fit(
        self,
        dataset: List[FASTAEncodedRecord],
        epochs: int = 10,
    ):
        pass
