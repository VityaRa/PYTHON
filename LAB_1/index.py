# Импорт необходимых функций
from math import *
from helpers import *
from errors import Errors
from tests import TEST_CASES, generate_test_results
import numpy as np
from enum import Enum

# Enum для облегчения работы с ошибками
class Errors(Enum):
    SUCCESS = 0
    INCORRECT_INPUT = 1
    UNDERROOT_INCORRECT_VALUE = 2
    DIVISION_BY_ZERO = 3

# Тексты для описания ошибок в зависимости от кода ошибки
ErrorText = {
    Errors.SUCCESS: '',
    Errors.INCORRECT_INPUT: 'Input values must be numbers',
    Errors.UNDERROOT_INCORRECT_VALUE: 'Value under the root cant take negative values',
    Errors.DIVISION_BY_ZERO: 'Division by zero'
}

# Минимальное значение для sin(x), чтобы считать sin(x) равным 0
MINIMAL_VALUE_FOR_PI_TO_EQUAL_ZERO = 1.2346467991473532e-16

def is_number(value):
    return type(value) == int or type(value) == float

def convert_to_numbers(x, y, z):
    error_code = None

    is_all_numbers = is_number(x) and is_number(y) and is_number(z)
    if not is_all_numbers:
        return Errors.INCORRECT_INPUT

    try:
        x = float(x)
        y = float(y)
        z = float(z)

        error_code = Errors.SUCCESS

    except ValueError:
        error_code = Errors.INCORRECT_INPUT

    finally:
        return error_code

def check_sinus_value(sinus_value):
    return sinus_value < MINIMAL_VALUE_FOR_PI_TO_EQUAL_ZERO and sinus_value > -MINIMAL_VALUE_FOR_PI_TO_EQUAL_ZERO or sinus_value == 0.0 or sinus_value == 0


def LAB1_VAR_4(x, y, z):
    # Объявление переменных для хранения промежуточных значений
    under_root_sum = None # Сумма под корнем
    sqrt_value = None # Значение корня
    sinus_value = None # Значение синуса
    abs_value = None # Модуль синуса
    division_value = None # Результат деления
    exponent_value = None # Результат возведенения экспоненты в степень
    result = None # Конечный результат 

    error_code = convert_to_numbers(x, y, z)
    if (error_code == Errors.INCORRECT_INPUT):
        return Errors.INCORRECT_INPUT

    under_root_sum = x + y
    if (under_root_sum < 0):
        return Errors.UNDERROOT_INCORRECT_VALUE

    sinus_value = np.sin(z)
    if ():
        return Errors.DIVISION_BY_ZERO

    sqrt_value = sqrt(under_root_sum)
    abs_value = abs(sinus_value)
    division_value = sqrt_value / abs_value
    exponent_value = exp(x)

    result = division_value + exponent_value
    # Если функция не возвращает ошибок, то возвращается результат выражения
    return result

def TEST_LAB1_VAR_4():
    tests_values = []
    
    for i in range(len(TEST_CASES)):
        x = TEST_CASES[i]['x']
        y = TEST_CASES[i]['y']
        z = TEST_CASES[i]['z']
        expected_value = TEST_CASES[i]['expect']
        result = LAB1_VAR_4(x, y, z) == expected_value
        tests_values.append(result)
    
    return tests_values

test_results = TEST_LAB1_VAR_4()
generate_test_results(test_results)

