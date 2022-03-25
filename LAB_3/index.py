from math import cos, pi

class Task:
    def __init__(self):
        pass

    def get_first_func_results(self, N):
        if not N:
            return 0
        result_array = []
        for i in range(1, N + 1):
            result = self.__sigma_function(i)
            result_array.append(result)

        return sum(result_array)

    def get_second_func_results(self, start, end, step):
        result_array = []

        x = start

        while (end + step != x):
            result = {'value': self.__first_func(x), 'argument': x}
            result_array.append(result)
            x += step

        return result_array

    def get_third_func_results(self, x):
        print(x)

    def get_factorial(self, value):
        result = 1
        for i in range(1, value + 1):
            result *= i

        return result

    def get_fibonacci(self, index):
        numbers = [1, 1]

        if index < 3:
            return 'wrong input'
        for i in range(2, index):
            next = numbers[i - 2] + numbers[i - 1]
            numbers.append(next)

        return numbers

    def get_sixth_func(self, N):
        if N < 1:
            return 'error'
        
        result = 0

        for i in range(1, N + 1):
            result += self.__sigma_function_2(i)
        
        return result

    def __sigma_function(self, x):
        return x + (-1)**x

    def __sigma_function_2(self, x):
        return x * 2 - 1
    
    def __first_func(self, x):
        return x**2 + 2* x - 1

    def __sin(self, x, e):
        print(x)

    def __get_eulers_value(self, x, i):
        return x ** i / self.get_factorial(i)

    def get_max_min(self, array):
        min, max = array[0], array[0]
        min_index, max_index = 0, 0
        for i in range(len(array)):
            if array[i] < min:
                min = array[i]
                min_index = i
            if array[i] > max:
                max = array[i]
                max_index = i
            

        return {
            'min': {
                'value': min,
                'index': min_index
            },
            'max': {
                'value': max,
                'index': max_index
            }
        }




def cosin(x):
    return cos(2 * pi * x)

def result(min, max, step):
    results = []
    x = min
    while (max >= x):
        y = cosin(x)
        result = {'value': y, 'argument': x}
        results.append(result)
        x += step

    return results

def LAB_3_VAR_4():
    a = 0
    b = 2
    h = 0.02

    print(result(a, b, h))

LAB_3_VAR_4()