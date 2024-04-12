def torch_uint8_to_float0to1(image):
    """
    When use scikit-image and opencv-image
    """
    # image = Your Code Here
    return image

def numpy_with_channelfirst_float_from_rgb_unbatched_to_gray_batched(image):
    """
    When use scikit-image and opencv-image
    """
    # image = Your Code Here
    return image


def numpy_float0to1_to_uint8(image):
    """
    When use scikit-image and opencv-image
    """
    # image = Your Code Here
    return image


def tf_rgb_to_gray_nonchannel(image):
    """
    When use scikit-image and opencv-image
    """
    # image = Your Code Here
    return image


def tf_gray_nonechannel_float32_to_channellast_float64(image):
    """
    When use scikit-image and opencv-image
    """
    # image = Your Code Here
    return image


def torch_channelfirst_unbatched_to_channlelast_batched(image):
    """
    When use scikit-image and opencv-image
    """
    # image = Your Code Here
    return image


def torch_rgb_from_batched_cpu_to_unbatched_gpu(image):
    """
    When use scikit-image and opencv-image
    """
    # image = Your Code Here
    return image


def numpy_gray_with_channal_last_to_pil_rgb(image):
    """
    When use scikit-image and opencv-image
    """
    # image = Your Code Here
    return image


two_steps_conversion_task_set = [
    ({"data_representation": "torch.tensor", "color_channel": 'rgb', "channel_order": 'channel first',
      "minibatch_input": False, "image_data_type": 'uint8', "device": 'cpu'},
     {"data_representation": "torch.tensor", "color_channel": 'rgb', "channel_order": 'channel first',
      "minibatch_input": False, "image_data_type": 'float32(0to1)', "device": 'cpu'},
     torch_uint8_to_float0to1),
    
    ({"data_representation": "numpy.ndarray", "color_channel": 'rgb', "channel_order": 'channel first',
      "minibatch_input": False, "image_data_type": 'float32(0to1)', "device": 'cpu'},
     {"data_representation": "numpy.ndarray", "color_channel": 'gray', "channel_order": 'channel first',
      "minibatch_input": True, "image_data_type": 'float32(0to1)', "device": 'cpu'},
     numpy_with_channelfirst_float_from_rgb_unbatched_to_gray_batched),
    
    ({"data_representation": "numpy.ndarray", "color_channel": 'rgb', "channel_order": 'channel first',
      "minibatch_input": False, "image_data_type": 'float32(0to1)', "device": 'cpu'},
     {"data_representation": "numpy.ndarray", "color_channel": 'rgb', "channel_order": 'channel first',
      "minibatch_input": False, "image_data_type": 'uint8', "device": 'cpu'},
     numpy_float0to1_to_uint8),

    ({"data_representation": "tf.tensor", "color_channel": 'rgb', "channel_order": 'channel last',
      "minibatch_input": False, "image_data_type": 'uint8', "device": 'cpu'},
     {"data_representation": "tf.tensor", "color_channel": 'gray', "channel_order": 'none',
      "minibatch_input": False, "image_data_type": 'uint8', "device": 'cpu'},
     tf_rgb_to_gray_nonchannel),

    ({"data_representation": "tf.tensor", "color_channel": 'gray', "channel_order": 'none',
      "minibatch_input": False, "image_data_type": 'float32(0to1)', "device": 'cpu'},
     {"data_representation": "tf.tensor", "color_channel": 'gray', "channel_order": 'channel last',
      "minibatch_input": False, "image_data_type": 'float64(0to1)', "device": 'cpu'},
     tf_gray_nonechannel_float32_to_channellast_float64),

    ({"data_representation": "tf.tensor", "color_channel": 'gray', "channel_order": 'none',
      "minibatch_input": False, "image_data_type": 'float32(0to1)', "device": 'cpu'},
     {"data_representation": "tf.tensor", "color_channel": 'gray', "channel_order": 'channel last',
      "minibatch_input": False, "image_data_type": 'float64(0to1)', "device": 'cpu'},
     tf_gray_nonechannel_float32_to_channellast_float64),

    ({"data_representation": "torch.tensor", "color_channel": 'rgb', "channel_order": 'channel first',
      "minibatch_input": True, "image_data_type": 'float32(0to1)', "device": 'cpu'},
     {"data_representation": "torch.tensor", "color_channel": 'rgb', "channel_order": 'channel first',
      "minibatch_input": False, "image_data_type": 'float32(0to1)', "device": 'gpu'},
     torch_rgb_from_batched_cpu_to_unbatched_gpu),

    ({"data_representation": "numpy.ndarray", "color_channel": 'gray', "channel_order": 'channel last',
      "minibatch_input": False, "image_data_type": 'uint8', "device": 'cpu'},
     {"data_representation": "PIL.Image", "color_channel": 'rgb', "channel_order": 'channel last',
      "minibatch_input": False, "image_data_type": 'uint8', "device": 'cpu'},
     numpy_gray_with_channal_last_to_pil_rgb),
]
