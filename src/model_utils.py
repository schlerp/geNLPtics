import keras.layers


def build_batchnorm_block(
    x: keras.layers.Layer,
    filters: int = 16,
    kernel: int = 3,
    stride: int = 1,
    ratio: int = 2,
    act: str = "elu",
    padding: str = "same",
):
    # dimensionality reduction
    x = keras.layers.Conv1D(
        filters // ratio,
        kernel_size=1,
        strides=stride,
        padding=padding,
    )(x)

    # convolution
    x = keras.layers.Conv1D(
        filters,
        kernel_size=kernel,
        strides=stride,
        padding=padding,
    )(x)

    # batch norm
    x = keras.layers.BatchNormalization()(x)
    # activation
    x = keras.layers.Activation(act)(x)

    return x
