# Give 3 numbers
# Get medium value ~medium~ = (v1 + v2 + v3) / 3
# Find minimal v[i] - medium

get_medium_value = lambda array: sum(array) / len(array)
get_range = lambda value, medium: value - medium    
get_minimal = lambda array: array.index(min(array))
get_compare_value = lambda value, medium: abs(get_range(value, medium)) 

def LAB_2_VAR_4():
    v1 = float(input('v1: '))
    v2 = float(input('v2: '))
    v3 = float(input('v3: '))

    array_values = [v1, v2, v3]
    medium = get_medium_value(array_values)

    range_1 = get_compare_value(array_values[0], medium)
    range_2 = get_compare_value(array_values[1], medium)
    range_3 = get_compare_value(array_values[2], medium)

    minimal = get_minimal([range_1, range_2, range_3])
    return array_values[minimal]

res = LAB_2_VAR_4()
print(res)