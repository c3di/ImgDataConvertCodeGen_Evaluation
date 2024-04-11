def numpy_bgr_uint8_to_rgb_float(image):
    """
    When use scikit-image and opencv-image
    """
    # image = Your Code Here
    return image


def tf_rgb_channelfirst_batched_to_gray_channellast_unbatched(image):
    """
    When use scikit-image and opencv-image
    """
    # image = Your Code Here
    return image


def tf_gray_uint8_nonechannel_to_rgb_float320to1_channellast(image):
    """
    When use scikit-image and opencv-image
    """
    # image = Your Code Here
    return image


def torch_channelfirst_float32_to_channellast_uint8(image):
    """
    When use scikit-image and opencv-image
    """
    # image = Your Code Here
    return image


def torch_rgb_gpu_to_numpy_gray_cpu(image):
    """
    When use scikit-image and opencv-image
    """
    # image = Your Code Here
    return image


three_steps_conversion_task_set = [
    ({"data_representation": "numpy.ndarray", "color_channel": 'bgr', "channel_order": 'channel first',
      "minibatch_input": False, "image_data_type": 'float32(0to1)', "device": 'cpu'},
     {"data_representation": "numpy.ndarray", "color_channel": 'rgb', "channel_order": 'channel first',
      "minibatch_input": False, "image_data_type": 'uint8', "device": 'cpu'},
     numpy_bgr_uint8_to_rgb_float),

    ({"data_representation": "numpy.ndarray", "color_channel": 'rgb', "channel_order": 'channel first',
      "minibatch_input": False, "image_data_type": 'float32(0to1)', "device": 'cpu'},
     {"data_representation": "numpy.ndarray", "color_channel": 'gray', "channel_order": 'channel first',
      "minibatch_input": True, "image_data_type": 'float32(0to1)', "device": 'cpu'},
     numpy_with_channelfirst_float_from_rgb_unbatched_to_gray_batched),

    ({"data_representation": "tf.tensor", "color_channel": 'rgb', "channel_order": 'channel first',
      "minibatch_input": True, "image_data_type": 'uint8', "device": 'cpu'},
     {"data_representation": "tf.tensor", "color_channel": 'gray', "channel_order": 'channel last',
      "minibatch_input": False, "image_data_type": 'uint8', "device": 'cpu'},
     tf_rgb_channelfirst_batched_to_gray_channellast_unbatched),

    ({"data_representation": "tf.tensor", "color_channel": 'gray', "channel_order": 'none',
      "minibatch_input": False, "image_data_type": 'uint8', "device": 'cpu'},
     {"data_representation": "tf.tensor", "color_channel": 'rgb', "channel_order": 'channel last',
      "minibatch_input": False, "image_data_type": 'float32(0to1)', "device": 'cpu'},
     tf_gray_uint8_nonechannel_to_rgb_float320to1_channellast),

    ({"data_representation": "torch.tensor", "color_channel": 'rgb', "channel_order": 'channel first',
      "minibatch_input": False, "image_data_type": 'float32(0to1)', "device": 'cpu'},
     {"data_representation": "torch.tensor", "color_channel": 'rgb', "channel_order": 'channel last',
      "minibatch_input": False, "image_data_type": 'uint8', "device": 'cpu'},
     torch_channelfirst_float32_to_channellast_uint8),

    ({"data_representation": "torch.tensor", "color_channel": 'rgb', "channel_order": 'channel first',
      "minibatch_input": False, "image_data_type": 'uint8', "device": 'gpu'},
     {"data_representation": "numpy.ndarray", "color_channel": 'gray', "channel_order": 'channel first',
      "minibatch_input": False, "image_data_type": 'uint8', "device": 'cpu'},
     torch_rgb_gpu_to_numpy_gray_cpu),
]
