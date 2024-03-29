import os.path

import numpy as np
import skimage as ski
import tensorflow as tf
import torch
from PIL import Image
from torchvision.transforms import functional as V1F
from torchvision.transforms.v2 import functional as V2F


test_image_path = os.path.join(os.path.dirname(__file__), "kodim15.png")
image = Image.open(test_image_path)
image_rgb = image.convert("RGB")
test_image = np.array(image_rgb)
assert test_image.shape[2] == 3
assert test_image.dtype == np.uint8
r = test_image[:, :, 0]
g = test_image[:, :, 1]
b = test_image[:, :, 2]
assert r.shape == g.shape == b.shape


def get_input_image_and_expected_output(source_metadata, target_metadata):
    is_gray_to_color = source_metadata["color_channel"] == "gray" and target_metadata["color_channel"] != "gray"
    print(get_test_images(source_metadata))
    return get_test_images(source_metadata), get_test_images(target_metadata, is_gray_to_color)


def get_test_images(source_metadata, is_gray_to_color=False):
    if source_metadata["data_representation"] == "numpy.ndarray":
        return get_numpy_image(source_metadata, is_gray_to_color)
    elif source_metadata["data_representation"] == "torch.tensor":
        return get_torch_image(source_metadata, is_gray_to_color)
    elif source_metadata["data_representation"] == "tf.tensor":
        return get_tensorflow_image(source_metadata, is_gray_to_color)
    elif source_metadata["data_representation"] == "PIL.Image":
        return get_pil_image(source_metadata, is_gray_to_color)
    else:
        raise ValueError(
            f"Unsupported data representation: {source_metadata['data_representation']}"
        )


def dtype_min_max(np_type):
    is_floating = np.issubdtype(np_type, np.floating)
    if is_floating:
        return np.finfo(np_type).min, np.finfo(np_type).max
    return np.iinfo(np_type).min, np.iinfo(np_type).max


def image_data_convert_with_scaled(source_np_type, target_np_type, img):
    s_min, s_max = dtype_min_max(source_np_type)
    t_min, t_max = dtype_min_max(target_np_type)

    source_range = s_max - s_min
    target_range = t_max - t_min
    adjusted_img = img - s_min
    scaled_img = (adjusted_img / source_range) * target_range + t_min
    return scaled_img.astype(target_np_type)


def get_numpy_image(source_metadata, is_gray_to_color=None):
    def is_invalid_numpy_metadata(metadata):
        return metadata["color_channel"] == "rgba" or metadata["color_channel"] == "graya" or metadata[
            "device"] == "gpu"

    is_invalid_numpy_metadata(source_metadata)

    img = np.stack([r, g, b], axis=0)  # [3, H, W] uint8 rgb channel first

    def convert_numpy_uint8_to_dtype(img, dtype):
        if dtype == "uint8":
            img = ski.util.img_as_ubyte(img)
        elif dtype == "uint16":
            img = ski.util.img_as_uint(img)
        elif dtype == "uint32":
            img = image_data_convert_with_scaled(img.dtype, np.uint32, img)
        elif dtype == "int8":
            img = image_data_convert_with_scaled(img.dtype, np.int8, img)
        elif dtype == "int16":
            img = ski.util.img_as_int(img)
        elif dtype == "int32":
            img = image_data_convert_with_scaled(img.dtype, np.int32, img)
        elif dtype == "float32(0to1)":
            img = ski.util.img_as_float32(img)
        elif dtype == "float32(-1to1)":
            img = ski.util.img_as_float32(img) * 2 - 1.0
        elif dtype == "float64(0to1)":
            img = ski.util.img_as_float64(img)
        elif dtype == "float64(-1to1)":
            img = ski.util.img_as_float64(img) * 2 - 1.0
        elif dtype == "double(0to1)":
            img = ski.util.img_as_float64(img)
        elif dtype == "double(-1to1)":
            img = ski.util.img_as_float64(img) * 2 - 1.0
        return img

    def color_to_grayscale(color_img_channle_first, color_channel):
        img = color_img_channle_first.copy()
        type_in = img.dtype
        if color_channel == 'rgb':
            img = 0.299 * img[0] + 0.587 * img[1] + 0.114 * img[2]
        elif color_channel == 'bgr':
            img = 0.299 * img[2] + 0.587 * img[1] + 0.114 * img[0]
        else:
            raise ValueError(f"Unsupported color channel: {color_channel}")
        img = np.expand_dims(img, axis=0)  # [1, H, W]
        return img.astype(type_in)

    def grayscale_to_rgb_or_bgr(img):
        img = np.repeat(img, repeats=3, axis=0)
        return img

    source_img = convert_numpy_uint8_to_dtype(img, source_metadata["image_data_type"])
    if source_metadata["color_channel"] == "gray":
        source_img = color_to_grayscale(source_img, 'rgb')  # [1, H, W]
    else:
        if is_gray_to_color:
            source_img = color_to_grayscale(source_img, 'rgb')
            source_img = grayscale_to_rgb_or_bgr(source_img)
        elif source_metadata["color_channel"] == "bgr":
            source_img = source_img[::-1, ...]

    def convert_other_attributes(img, metadata):
        if metadata is None:
            return None
        # img [3, H, W] or [1, H, W]
        if metadata["color_channel"] == "gray" and metadata["channel_order"] == "none":
            img = np.squeeze(img, axis=0)  # [H, W]
        elif metadata["channel_order"] == "channel last":
            img = np.transpose(img, (1, 2, 0))  # [H, W, 3] or [H, W, 1]
        if metadata["minibatch_input"]:
            img = img[np.newaxis, ...]

        return img

    return convert_other_attributes(source_img, source_metadata)


def get_torch_image(source_metadata, is_gray_to_color=None):
    source_img = torch.stack([torch.from_numpy(r), torch.from_numpy(g), torch.from_numpy(b)], dim=0)  # [3, H, W] uint8
    source_img = torch_to_dtype(source_img, source_metadata)
    if source_metadata["color_channel"] == "gray":
        source_img = V1F.rgb_to_grayscale(source_img)  # [1, H, W]
    else:
        if is_gray_to_color:
            source_img = V1F.rgb_to_grayscale(source_img)
            source_img = source_img.repeat(3, 1, 1)  # [3, H, W]

    def convert_other_attributes(img, metadata):
        if metadata is None:
            return None
        # img [3, H, W] or [1, H, W]
        if metadata["color_channel"] == "gray":
            if metadata["channel_order"] == "channel last":
                img = img.permute(1, 2, 0)  # [H, W, 1]
            elif metadata["channel_order"] == "none":
                img = img.squeeze(0)  # [H, W]
        elif metadata["color_channel"] == "rgb" and metadata["channel_order"] == "channel last":
            img = img.permute(1, 2, 0)  # [H, W, 3]

        if metadata["minibatch_input"]:
            img = img.unsqueeze(0)
        if metadata["device"] == "gpu":
            img = img.cuda()
        return img

    return convert_other_attributes(source_img, source_metadata)


def torch_to_dtype(source_img, metadata):
    # Slightly different from V1F.to_dtype and this is more common conversion code between uint8 and float32
    if source_img.dtype == torch.uint8 and metadata["image_data_type"] == "float32(0to1)":
        return (source_img / 255.0).to(torch.float32)
    elif source_img.dtype == torch.float32 and metadata["image_data_type"] == "uint8":
        return (source_img * 255).to(torch.uint8)
    else:
        dtype_mapping = {
            "uint8": torch.uint8,
            "int8": torch.int8,
            "int16": torch.int16,
            "int32": torch.int32,
            "int64": torch.int64,
            "float32(0to1)": torch.float32,
            "float64(0to1)": torch.double,
            "double(0to1)": torch.double,
        }
        return V2F.to_dtype(source_img, dtype_mapping[metadata["image_data_type"]], scale=True)


def get_tensorflow_image(source_metadata, is_gray_to_color=None):
    source_img = tf.stack([tf.convert_to_tensor(r / 255.0, dtype=tf.float32),
                           tf.convert_to_tensor(g / 255.0, dtype=tf.float32),
                           tf.convert_to_tensor(b / 255.0, dtype=tf.float32), ],
                          axis=-1)  # [H, W, 3] float32 rgb channel last

    dtype_mapping = {
        "uint8": tf.uint8,
        "uint16": tf.uint16,
        "uint32": tf.uint32,
        "uint64": tf.uint64,
        "int8": tf.int8,
        "int16": tf.int16,
        "int32": tf.int32,
        "int64": tf.int64,
        "float16(0to1)": tf.float16,
        "float32(0to1)": tf.float32,
        "float64(0to1)": tf.float64,
        "double(0to1)": tf.float64,
    }

    source_img = tf.image.convert_image_dtype(source_img, dtype=dtype_mapping[source_metadata["image_data_type"]])
    if source_metadata["color_channel"] == "gray":
        source_img = tf.image.rgb_to_grayscale(source_img)  # [H, W, 1]
    else:
        if is_gray_to_color:
            source_img = tf.image.rgb_to_grayscale(source_img)
            source_img = tf.image.grayscale_to_rgb(source_img)

    def convert_other_attributes(img, metadata):
        if metadata is None:
            return None
        # img [H, W, 3] or [H, W, 1]
        if metadata["color_channel"] == "gray" and metadata["channel_order"] == "none":
            img = tf.squeeze(img, axis=-1)  # [H, W]
        elif metadata["color_channel"] in ["rgb", "gray"] and metadata["channel_order"] == "channel first":
            img = tf.transpose(img, perm=[2, 0, 1])  # [3, H, W] or [1, H, W]

        if metadata["minibatch_input"]:
            img = tf.expand_dims(img, 0)

        if metadata['device'] == 'gpu':
            img = img.gpu()
        return img

    return convert_other_attributes(source_img, source_metadata)


def get_pil_image(source_metadata, is_gray_to_color=None):
    def is_invalid_pil_metadata(metadata):
        return metadata["minibatch_input"] or metadata["image_data_type"] != 'uint8' or metadata["device"] == 'gpu' or \
            metadata["channel_order"] == 'channel first'

    is_invalid_pil_metadata(source_metadata)

    img_array = np.stack([r, g, b], axis=-1)
    base_img = Image.fromarray(img_array, mode='RGB')  # [H, W, 3] uint8 rgb channel last

    def convert_color_channel_channel_order(img, metadata):
        if metadata is None:
            return None
        if metadata["color_channel"] == "gray" and metadata['channel_order'] == 'none':
            img = img.convert('L')  # [H, W]
        if metadata["color_channel"] == "rgb" and metadata['channel_order'] == 'channel last':
            if is_gray_to_color:
                img = img.convert('L')

            img = img.convert('RGB')  # [H, W, 3]
        elif metadata["color_channel"] == "rgba":
            img = img.convert('RGBA')
        elif metadata["color_channel"] == "graya":
            img = img.convert('LA')  # [H, W, 2]
        return img

    return convert_color_channel_channel_order(base_img, source_metadata)


def is_tensorflow_image_equal(image1, image2, tolerance=1e-5):
    equality = tf.math.equal(image1, image2)
    if image1.dtype.is_floating:
        close_enough = tf.less_equal(tf.abs(image1 - image2), tolerance)
        combined_check = tf.logical_or(equality, close_enough)
    else:
        combined_check = equality
    return tf.reduce_all(combined_check)


def is_image_equal(image1, image2, tolerance=2):
    # When converting color images to grayscale or changing the data type of an array, the pixel values often undergo
    # transformations that can result in minor discrepancies due to the nature of the computations involved.
    # For instance, color-to-grayscale conversion involves a weighted sum of the RGB channels, which might not be
    # perfectly reversible, especially when rounding is involved in the process. Similarly, changing the data type,
    # such as from a float to an integer, can lead to rounding errors or truncation.
    # To accommodate these potential variations in pixel values and ensure a pragmatic comparison, 
    # we select a higher tolerance value
    try:
        if type(image1) != type(image2):
            return False
        if isinstance(image1, np.ndarray):
            return np.allclose(image1, image2, tolerance)
        elif isinstance(image1, torch.Tensor):
            return torch.allclose(image1, image2, rtol=tolerance, atol=tolerance)
        elif isinstance(image1, tf.Tensor):
            return is_tensorflow_image_equal(image1, image2, tolerance)
        elif isinstance(image1, Image.Image):
            return np.allclose(np.array(image1), np.array(image2), tolerance)
    except Exception:
        pass
    return False
