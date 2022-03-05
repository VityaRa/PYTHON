from errors import Errors
minimal_value_for_pi = 1.2346467991473532e-16

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