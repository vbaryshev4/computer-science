import math

class Point(object):
    """docstring for Point"""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

        if x != 0 and y != 0:
            self.r = self.__distance(Point())
        else:
            self.r = 0

    def __distance(self, p):
        if isinstance(p, Point):
            return math.sqrt((self.x-p.x)**2+(self.y-p.y)**2)
        else:
            raise TypeError('argument is not a Point')

    def scolar(self, p):
        if isinstance(p, Point):
            x = self.x + p.x
            y = self.y + p.y
            return Point(x, y)
        else:
            raise TypeError('argument is not a Point')

    def scolar_mul(self, num):
        x = self.x * num
        y = self.y * num
        return Point(x, y)

    def distance(self, p):
        return self.__distance(p)

    def belongs(self, func):
        return self.y == func(self.x)

    def quadrant(self):
        x = self.x
        y = self.y
        
        if x > 0 and y > 0:
            return '1 квадрант'
        if x < 0 and y > 0:
            return '2 квадрант'
        if x < 0 and y < 0:
            return '3 квадрант'
        if x > 0 and y < 0:
            return '4 квадрант'
           









