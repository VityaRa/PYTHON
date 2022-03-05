from errors import Errors
from math import pi

TEST_CASES = [
    {
        'x': 1,
        'y': 2,
        'z': 3,
        'expect': 14.991883788813885,
    },
    {
        'x': "",
        'y': 2,
        'z': 3,
        'expect': Errors.INCORRECT_INPUT,
    },
    {
        'x': "",
        'y': "",
        'z': "",
        'expect': Errors.INCORRECT_INPUT,
    },
    {
        'x': 2,
        'y': 4,
        'z': 0,
        'expect': Errors.DIVISION_BY_ZERO,
    },
    {
        'x': 2,
        'y': 4,
        'z': pi,
        'expect': Errors.DIVISION_BY_ZERO,
    },
    {
        'x': 1,
        'y': -2,
        'z': 2,
        'expect': Errors.UNDERROOT_INCORRECT_VALUE,
    },
    {
        'x': "12.0",
        'y': 3,
        'z': 4,
        'expect': Errors.INCORRECT_INPUT,
    },
    {
        'x': "12.0",
        'y': '123',
        'z': '142',
        'expect': Errors.INCORRECT_INPUT,
    },
]

def generate_test_results(test_results = []):
    array_length = len(test_results)
    for i in range(array_length):
        result = 'passed' if test_results[i] else 'failed'
        print('Test {} {}'.format(i + 1, result))