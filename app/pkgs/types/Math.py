import math

coords = []

def create_coord(x, y):
    values = {'x': x, 'y': y}
    return coords.append(values)

def get_xny(point):
    x = point.get('x')
    y = point.get('y')
    return (x, y)

def scolar_sum(point_1, point_2):
    x1,y1 = get_xny(point_1)
    x2,y2 = get_xny(point_1)
    return {'new_x':x1+x2, 'new_y':y1+y2}

def scolar_mul(point, digit):
    x,y = get_xny(point)
    return {'new_x':x*digit, 'new_y':y*digit}

def distance(point_1, point_2):
    x1,y1 = get_xny(point_1)
    x2,y2 = get_xny(point_2)
    return {'distance': math.sqrt((x1-x2)**2+(y1-y2)**2)}

def belongs(point, func):
    x,y = get_xny(point)
    if y == func(x):
        return 'Ok'
    else:
        return 'Do not belongs'

def parabol(x):
    return x ** 2

def quadrant(point):
    x,y = get_xny(point)
    if (x>0) and (y>0):
        return '1 квадрант'
    if (x<0) and (y>0):
        return '2 квадрант'
    if (x<0) and (y<0):
        return '3 квадрант'
    if (x>0) and (y<0):
        return '4 квадрант'


create_coord(1,3)
create_coord(4,5)
create_coord(-44,55)
create_coord(434,-11)
print(coords)

print(scolar_sum(coords[0], coords[1]))
print(scolar_sum(coords[2], coords[3]))

print(scolar_mul(coords[0], 2))
print(scolar_mul(coords[1], 2))
print(scolar_mul(coords[2], 2))
print(scolar_mul(coords[3], 2))

print(distance(coords[0], coords[1]))
print(distance(coords[2], coords[3]))

print(belongs(coords[0], parabol))
print(belongs(coords[1], parabol))
print(belongs(coords[2], parabol))
print(belongs(coords[3], parabol))

print(quadrant(coords[0]))
print(quadrant(coords[1]))
print(quadrant(coords[2]))
print(quadrant(coords[3]))
