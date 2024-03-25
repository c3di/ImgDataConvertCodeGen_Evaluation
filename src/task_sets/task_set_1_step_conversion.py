def numpy_rgb_to_opencv_bgr(image):
    """
    When use scikit-image and opencv-image
    """
    # image = Your Code Here
    return image


def numpy_channel_first_to_last(image):
    """
    When use scikit-image and opencv-image
    """
    # image = Your Code Here
    return image


def tf_batched_to_unbatched(image):
    """
    When use scikit-image and opencv-image
    """
    # image = Your Code Here
    return image


def torch_uint8_to_float0to1(image):
    """
    When use scikit-image and opencv-image
    """
    # image = Your Code Here
    return image


def torch_gpu_to_cpu(image):
    """
    When use scikit-image and opencv-image
    """
    # image = Your Code Here
    return image


def pil_to_tf(image):
    """
    When use scikit-image and opencv-image
    """
    # image = Your Code Here
    return image


one_step_conversion_task_set = [
    ({"data_representation": "numpy.ndarray", "color_channel": 'rgb', "channel_order": 'channel first',
      "minibatch_input": False, "image_data_type": 'uint8', "device": 'cpu'},
     {"data_representation": "numpy.ndarray", "color_channel": 'bgr', "channel_order": 'channel first',
      "minibatch_input": False, "image_data_type": 'uint8', "device": 'cpu'},
     numpy_rgb_to_opencv_bgr),

    ({"data_representation": "numpy.ndarray", "color_channel": 'rgb', "channel_order": 'channel first',
      "minibatch_input": False, "image_data_type": 'uint8', "device": 'cpu'},
     {"data_representation": "numpy.ndarray", "color_channel": 'rgb', "channel_order": 'channel last',
      "minibatch_input": False, "image_data_type": 'uint8', "device": 'cpu'},
     numpy_channel_first_to_last),

    ({"data_representation": "tf.tensor", "color_channel": 'rgb', "channel_order": 'channel last',
      "minibatch_input": True, "image_data_type": 'uint8', "device": 'cpu'},
     {"data_representation": "tf.tensor", "color_channel": 'rgb', "channel_order": 'channel last',
      "minibatch_input": False, "image_data_type": 'uint8', "device": 'cpu'},
     tf_batched_to_unbatched),

    ({"data_representation": "torch.tensor", "color_channel": 'rgb', "channel_order": 'channel first',
      "minibatch_input": False, "image_data_type": 'uint8', "device": 'cpu'},
     {"data_representation": "torch.tensor", "color_channel": 'rgb', "channel_order": 'channel first',
      "minibatch_input": False, "image_data_type": 'float32(0to1)', "device": 'cpu'},
     torch_uint8_to_float0to1),

    ({"data_representation": "torch.tensor", "color_channel": 'rgb', "channel_order": 'channel first',
      "minibatch_input": False, "image_data_type": 'uint8', "device": 'gpu'},
     {"data_representation": "torch.tensor", "color_channel": 'rgb', "channel_order": 'channel first',
      "minibatch_input": False, "image_data_type": 'uint8', "device": 'cpu'},
     torch_gpu_to_cpu),

    ({"data_representation": "PIL.Image", "color_channel": 'rgb', "channel_order": 'channel last',
      "minibatch_input": False, "image_data_type": 'uint8', "device": 'cpu'},
     {"data_representation": "tf.tensor", "color_channel": 'rgb', "channel_order": 'channel last',
      "minibatch_input": False, "image_data_type": 'uint8', "device": 'cpu'},
     pil_to_tf)]
