from math import *
from helpers import *
from errors import Errors
from tests import TEST_CASES, generate_test_results
import numpy as np
# O(1)

def LAB1_VAR_4(x, y, z):
    under_root_sum = None
    sqrt_value = None
    sinus_value = None
    abs_value = None
    division_value = None
    exponent_value = None
    result = None

    error_code = convert_to_numbers(x, y, z)
    if (error_code == Errors.INCORRECT_INPUT):
        return Errors.INCORRECT_INPUT

    under_root_sum = x + y
    if (under_root_sum < 0):
        return Errors.UNDERROOT_INCORRECT_VALUE

    sinus_value = np.sin(z)
    if (sinus_value < minimal_value_for_pi and sinus_value > -minimal_value_for_pi or sinus_value == 0.0 or sinus_value == 0):
        return Errors.DIVISION_BY_ZERO

    sqrt_value = sqrt(under_root_sum)
    abs_value = abs(sinus_value)
    division_value = sqrt_value / abs_value
    exponent_value = exp(x)

    result = division_value + exponent_value
    return result

# result = LAB1_VAR_4(1, 2, 3)
# print(result)

def TEST_LAB1_VAR_4():
    tests_values = []

    for i in range(len(TEST_CASES)):
        x = TEST_CASES[i]['x']
        y = TEST_CASES[i]['y']
        z = TEST_CASES[i]['z']
        expected_value = TEST_CASES[i]['expect']
        # print(LAB1_VAR_4(x, y, z))
        result = LAB1_VAR_4(x, y, z) == expected_value
        tests_values.append(result)
    
    return tests_values

test_results = TEST_LAB1_VAR_4()
generate_test_results(test_results)

