from math import sin, pi

min = -1
max = 6
step = 0.1

class FunctionFactory:
    def __init__(self):
        pass

    def get_first(x):
        return sin(2 * pi * x)
    
    def get_second(x):
        return x ** 2 + 2

    def get_third(x):
        return -x ** 2 + 2

    def get_index(x):
        if x <= 0:
            return 1
        if x >= 0 and x <= 3:
            return 2
        if x > 3:
            return 3

    def run(self, x):
        index = self.get_index(x)
        if index == 1:
            return self.get_first(x)
        if index == 2:
            return self.get_second(x)
        if index == 3:
            return self.get_third(x)

def LAB_4_VAR4(a, b, h):
    current = a
    results_array = []

    function_factory = FunctionFactory()

    while current <= b:
        result = FunctionFactory.run(current)
        results_array.append({"arg": current, "result": result})
        current += h

    return results_array

res = LAB_4_VAR4(min, max, step)
print(res)