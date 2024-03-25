def numpy_bgr_channelfirst_unbatched_uint8_to_tf_rgb_channellast_batched_float0to1(image):
    """
    When use scikit-image and opencv-image
    """
    # image = Your Code Here
    return image


def numpy_rgb_channelfirst_batched_float0to1_to_PIL_rgb_channellast_unbatched_uint8(image):
    """
    When use scikit-image and opencv-image
    """
    # image = Your Code Here
    return image


def PIL_gray_nonechannel_unit8_to_tf_rgb_float32_channellast_batched(image):
    """
    When use scikit-image and opencv-image
    """
    # image = Your Code Here
    return image


def tf_gray_channellast_batced_gpu_to_torch_rgb_channelfirst_batched_cpu(image):
    """
    When use scikit-image and opencv-image
    """
    # image = Your Code Here
    return image


def torch_rgb_uint8_batched_gpu_to_numpy_gray_float_batched_nonechannel_cpu(image):
    """
    When use scikit-image and opencv-image
    """
    # image = Your Code Here
    return image


def torch_gray_float32_channelfirst_batched_gpu_to_tf_gray_nonnchannel_float_unbatched_gpu(image):
    """
    When use scikit-image and opencv-image
    """
    # image = Your Code Here
    return image


more_steps_conversion_task_set = [
    ({"data_representation": "numpy.ndarray", "color_channel": 'bgr', "channel_order": 'channel first',
      "minibatch_input": False, "image_data_type": 'uint8', "device": 'cpu'},
     {"data_representation": "tf.tensor", "color_channel": 'rgb', "channel_order": 'channel last',
      "minibatch_input": True, "image_data_type": 'float32(0to1)', "device": 'cpu'},
     numpy_bgr_channelfirst_unbatched_uint8_to_tf_rgb_channellast_batched_float0to1),

    ({"data_representation": "numpy.ndarray", "color_channel": 'rgb', "channel_order": 'channel first',
      "minibatch_input": True, "image_data_type": 'float32(0to1)', "device": 'cpu'},
     {"data_representation": "PIL.Image", "color_channel": 'rgb', "channel_order": 'channel last',
      "minibatch_input": False, "image_data_type": 'uint8', "device": 'cpu'},
     numpy_rgb_channelfirst_batched_float0to1_to_PIL_rgb_channellast_unbatched_uint8),

    ({"data_representation": "PIL.Image", "color_channel": 'gray', "channel_order": 'none',
      "minibatch_input": False, "image_data_type": 'uint8', "device": 'cpu'},
     {"data_representation": "tf.tensor", "color_channel": 'rgb', "channel_order": 'channel last',
      "minibatch_input": True, "image_data_type": 'float32(0to1)', "device": 'cpu'},
     PIL_gray_nonechannel_unit8_to_tf_rgb_float32_channellast_batched),

    ({"data_representation": "tf.tensor", "color_channel": 'gray', "channel_order": 'channel last',
      "minibatch_input": True, "image_data_type": 'float32(0to1)', "device": 'gpu'},
     {"data_representation": "torch.tensor", "color_channel": 'rgb', "channel_order": 'channel first',
      "minibatch_input": True, "image_data_type": 'float32(0to1)', "device": 'cpu'},
     tf_gray_channellast_batced_gpu_to_torch_rgb_channelfirst_batched_cpu),

    ({"data_representation": "torch.tensor", "color_channel": 'rgb', "channel_order": 'channel first',
      "minibatch_input": True, "image_data_type": 'uint8', "device": 'gpu'},
     {"data_representation": "numpy.ndarray", "color_channel": 'gray', "channel_order": 'none',
      "minibatch_input": True, "image_data_type": 'float32(0to1)', "device": 'cpu'},
     torch_rgb_uint8_batched_gpu_to_numpy_gray_float_batched_nonechannel_cpu),

    ({"data_representation": "torch.tensor", "color_channel": 'gray', "channel_order": 'channel first',
      "minibatch_input": True, "image_data_type": 'float32(0to1)', "device": 'gpu'},
     {"data_representation": "tf.tensor", "color_channel": 'gray', "channel_order": 'none',
      "minibatch_input": False, "image_data_type": 'float32(0to1)', "device": 'gpu'},
     torch_gray_float32_channelfirst_batched_gpu_to_tf_gray_nonnchannel_float_unbatched_gpu),
]
