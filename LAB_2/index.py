LIST_LENGTH = 3

get_medium_value = lambda array: sum(array) / len(array)
get_range = lambda value, medium: value - medium    
get_minimal_index = lambda array: array.index(min(array))
get_compare_value = lambda value, medium: abs(get_range(value, medium)) 

def generate_error():
    return None, None, None

def is_number(value):
    return type(value) == int or type(value) == float

def convert_to_numbers(v1, v2, v3):
    if is_number(v1) and is_number(v2) and is_number(v3):
        return float(v1), float(v2), float(v3)
    else:
        return generate_error()



def LAB_2_VAR_4(list):
    if len(list) != LIST_LENGTH:
        return 'error: wrong input count'

    number1, number2, number3 = convert_to_numbers(list[0], list[1], list[2])
    if number1 == None:
        return 'error: wrong input'
    
    array_values = [number1, number2, number3]
    medium = get_medium_value(array_values)

    range_1 = get_compare_value(array_values[0], medium)
    range_2 = get_compare_value(array_values[1], medium)
    range_3 = get_compare_value(array_values[2], medium)

    minimal = get_minimal_index([range_1, range_2, range_3])
    return array_values[minimal]

res = LAB_2_VAR_4([0, 0, 1])
print(res)