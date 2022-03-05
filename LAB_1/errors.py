from enum import Enum

class Errors(Enum):
    SUCCESS = 0
    INCORRECT_INPUT = 1
    UNDERROOT_INCORRECT_VALUE = 2
    DIVISION_BY_ZERO = 3

ErrorText = {
    Errors.SUCCESS: '',
    Errors.INCORRECT_INPUT: 'Input values must be numbers',
    Errors.UNDERROOT_INCORRECT_VALUE: 'Value under the root cant take negative values',
    Errors.DIVISION_BY_ZERO: 'Division by zero'
}
