# . Заданы координаты трех точек (x1,y1), (x2,y2) и (x3,y3). Найдите площадь
# треугольника образованного данными точками (по формуле Герона)

from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Side:
    def __init__(self, point1: Point, point2: Point):
        self.length = sqrt((point2.x - point1.x) ** 2  + (point2.y - point1.y) ** 2)

class Triangle:
    def __init__(self, side1: Side, side2: Side, side3: Side):
        self.sides = [side1, side2, side3]

    def get_perimeter(self):
        perimeter = 0
        for side in self.sides:
            perimeter += side.length
        return perimeter

    def get_half_perimiter(self):
        return self.get_perimeter() / len(self.sides)

    def get_area(self):
        p = self.get_half_perimiter()
        return sqrt(p * (p - self.sides[0].length) * (p - self.sides[1].length) * (p - self.sides[2].length)) 

def LAB_1_VAR_1(x1, y1, x2, y2, x3, y3):
    print('input values:')
    print('x1: ', x1, ' ', 'y1: ', y1)
    print('x2: ', x2, ' ', 'y2: ', y2)
    print('x3: ', x3, ' ', 'y3: ', y3)

    point1 = Point(x1, y1)
    point2 = Point(x2, y2)
    point3 = Point(x3, y3)

    triangle = Triangle(Side(point1, point2), Side(point1, point3), Side(point1, point3))
    area = triangle.get_area()

    return area

area = LAB_1_VAR_1(1, 2, 0, 0, 5, 5)
print(area)