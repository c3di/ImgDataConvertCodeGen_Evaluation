def numpy_gray_nonechannel_unbatched_uint8_to_rgb_channelfirst_batched_float0to1(image):
    """
    When use scikit-image and opencv-image
    """
    # image = Your Code Here
    return image


def numpy_rgb_channelfirst_batched_float0to1_to_rgb_channellast_unbatched_uint8(image):
    """
    When use scikit-image and opencv-image
    """
    # image = Your Code Here
    return image


def tf_rgb_uint8_unbatched_channellast_to_gray_float320to1_batched_nonechannel(image):
    """
    When use scikit-image and opencv-image
    """
    # image = Your Code Here
    return image


def tf_gray_float32_channellast_batched_to_rgb_chanelfirst_unit8_unbatched(image):
    """
    When use scikit-image and opencv-image
    """
    # image = Your Code Here
    return image


def torch_rgb_uint8_batched_channelfirst_gpu_to_float_unbatched_channellast_cpu(image):
    """
    When use scikit-image and opencv-image
    """
    # image = Your Code Here
    return image


def torch_rgb_channelfirst_batched_float_to_tf_gray_batched_channellast_float(image):
    """
    When use scikit-image and opencv-image
    """
    # image = Your Code Here
    return image


four_steps_conversion_task_set = [
    ({"data_representation": "numpy.ndarray", "color_channel": 'gray', "channel_order": 'none',
      "minibatch_input": False, "image_data_type": 'uint8', "device": 'cpu'},
     {"data_representation": "numpy.ndarray", "color_channel": 'rgb', "channel_order": 'channel first',
      "minibatch_input": True, "image_data_type": 'float32(0to1)', "device": 'cpu'},
     numpy_gray_nonechannel_unbatched_uint8_to_rgb_channelfirst_batched_float0to1),

    ({"data_representation": "numpy.ndarray", "color_channel": 'rgb', "channel_order": 'channel first',
      "minibatch_input": True, "image_data_type": 'float32(0to1)', "device": 'cpu'},
     {"data_representation": "numpy.ndarray", "color_channel": 'rgb', "channel_order": 'channel last',
      "minibatch_input": False, "image_data_type": 'uint8', "device": 'cpu'},
     numpy_rgb_channelfirst_batched_float0to1_to_rgb_channellast_unbatched_uint8),

    ({"data_representation": "tf.tensor", "color_channel": 'rgb', "channel_order": 'channel last',
      "minibatch_input": False, "image_data_type": 'uint8', "device": 'cpu'},
     {"data_representation": "tf.tensor", "color_channel": 'gray', "channel_order": 'none',
      "minibatch_input": True, "image_data_type": 'float32(0to1)', "device": 'cpu'},
     tf_rgb_uint8_unbatched_channellast_to_gray_float320to1_batched_nonechannel),

    ({"data_representation": "tf.tensor", "color_channel": 'gray', "channel_order": 'channel last',
      "minibatch_input": True, "image_data_type": 'float32(0to1)', "device": 'cpu'},
     {"data_representation": "tf.tensor", "color_channel": 'rgb', "channel_order": 'channel first',
      "minibatch_input": False, "image_data_type": 'uint8', "device": 'cpu'},
     tf_gray_float32_channellast_batched_to_rgb_chanelfirst_unit8_unbatched),

    ({"data_representation": "torch.tensor", "color_channel": 'rgb', "channel_order": 'channel first',
      "minibatch_input": True, "image_data_type": 'uint8', "device": 'gpu'},
     {"data_representation": "torch.tensor", "color_channel": 'rgb', "channel_order": 'channel last',
      "minibatch_input": False, "image_data_type": 'float32(0to1)', "device": 'cpu'},
     torch_rgb_uint8_batched_channelfirst_gpu_to_float_unbatched_channellast_cpu),

    ({"data_representation": "torch.tensor", "color_channel": 'rgb', "channel_order": 'channel first',
      "minibatch_input": True, "image_data_type": 'float32(0to1)', "device": 'cpu'},
     {"data_representation": "tf.tensor", "color_channel": 'gray', "channel_order": 'channel last',
      "minibatch_input": True, "image_data_type": 'float32(0to1)', "device": 'cpu'},
     torch_rgb_channelfirst_batched_float_to_tf_gray_batched_channellast_float),
]
