from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def check_correct_coordinates(self):
        return (type(self.x) == int or type(self.x) == float) and (type(self.y) == int or type(self.y) == float)

class Side:
    def __init__(self, point1: Point, point2: Point):
        self.length = sqrt((point2.x - point1.x) ** 2  + (point2.y - point1.y) ** 2)

class Triangle:
    def __init__(self, point1: Point, point2: Point, point3: Point):
        self.points = [point1, point2, point3]
        self.sides = [Side(point1, point2), Side(point1, point3), Side(point2, point3)]

    def get_perimeter(self):
        perimeter = 0
        for side in self.sides:
            perimeter += side.length
        return perimeter

    def get_area(self):
        if not self.__is_points_idempontency(): #or not self.__is_correct_coordinates():
            return 'Error: Одна из сторон имеет нулевую длину'
        else:
            p = self.get_perimeter() / 2
            area = sqrt(p * (p - self.sides[0].length) * (p - self.sides[1].length) * (p - self.sides[2].length)) 
            if not area:
                return area
            else:
                return 'Error: все точки лежат на одной прямой'
    def get_x(self):
        return [self.points[0].x, self.points[1].x, self.points[2].x]

    def get_y(self):
        return [self.points[0].y, self.points[1].y, self.points[2].y]

    def __is_points_idempontency(self):
        for side in self.sides:
            if side.length == 0:
                return False
    
        return True 


def LAB_1_VAR_4(x1, y1, x2, y2, x3, y3):

    point1 = Point(x1, y1)
    point2 = Point(x2, y2)
    point3 = Point(x3, y3)

    area = None

    if point1.check_correct_coordinates() and point2.check_correct_coordinates() and point3.check_correct_coordinates():
        triangle = Triangle(point1, point2, point3)
        area = triangle.get_area()
    else:
        area = 'Error: Неправильные точки'

    return area

area = LAB_1_VAR_4(0, 1, 2, 3, 4, 5)

# def TEST():
#     if LAB_1_VAR_4(3, 1, 2, 3, 4, 5) == 3.0000000000000013:
#         print('Тест 1 пройден')
#     else:
#         print('Тест 1 не пройден')

# TEST()

print(area)