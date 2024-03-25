from src.get_image_data import get_input_image_and_expected_output, is_image_equal


def is_cvt_func_correct(config):
    input_metadata, expected_metadata, test_func = config
    input_img, expected_image = get_input_image_and_expected_output(input_metadata, expected_metadata)
    return is_image_equal(test_func(input_img), expected_image)


def test_conversion_functions(tests_config, test_title: str = ''):
    wrong_tests = [config for config in tests_config if not is_cvt_func_correct(config)]
    print(test_title)
    print(f"Passed/Total: {len(tests_config) - len(wrong_tests)}/{len(tests_config)}")
    if wrong_tests:
        print("Failed Tests:")
        for wrong in wrong_tests:
            print(f'\t{wrong}')
